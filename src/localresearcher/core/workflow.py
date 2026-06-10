"""Workflow orchestrator for agent execution."""

from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from localresearcher.core.schemas import (
    Task,
    WorkflowState,
    AgentStep,
    AgentOutput,
    Report,
)
from localresearcher.llm.ollama import OllamaProvider
from localresearcher.rag.vector_store import VectorStore
from localresearcher.rag.loader import load_document
from localresearcher.agents.planner import PlannerAgent
from localresearcher.agents.researcher import ResearcherAgent
from localresearcher.agents.analyst import AnalystAgent
from localresearcher.agents.critic import CriticAgent
from localresearcher.agents.writer import WriterAgent


class ResearchWorkflow:
    """Orchestrates the multi-agent research workflow."""
    
    def __init__(self):
        self.console = Console()
        self.llm = OllamaProvider()
        self.vector_store = VectorStore()
        
        # Initialize agents
        self.planner = PlannerAgent(self.llm)
        self.researcher = ResearcherAgent(self.llm, self.vector_store)
        self.analyst = AnalystAgent(self.llm)
        self.critic = CriticAgent(self.llm)
        self.writer = WriterAgent(self.llm)
    
    async def check_ollama(self) -> bool:
        """Check if Ollama is available."""
        is_available = await self.llm.is_available()
        if not is_available:
            self.console.print(
                Panel(
                    "[red]Ollama is not available or model is not installed.[/red]\n\n"
                    f"Please ensure Ollama is running and the model '{self.llm.model}' is installed:\n"
                    f"  ollama pull {self.llm.model}",
                    title="❌ Connection Error",
                    border_style="red",
                )
            )
        return is_available
    
    async def load_documents(self, file_paths: list[Path]) -> Task:
        """Load documents and create a task."""
        documents = []
        
        for path in file_paths:
            if not path.exists():
                self.console.print(f"[yellow]Warning: File not found: {path}[/yellow]")
                continue
            
            try:
                doc = load_document(path)
                documents.append(doc)
                await self.vector_store.add_document(doc)
            except Exception as e:
                self.console.print(f"[yellow]Warning: Failed to load {path}: {e}[/yellow]")
        
        return Task(query="", documents=documents)
    
    async def execute(self, query: str, file_paths: list[Path] | None = None) -> Report:
        """Execute the full research workflow."""
        # Check Ollama availability
        if not await self.check_ollama():
            raise RuntimeError("Ollama is not available")
        
        # Load documents if provided
        task = Task(query=query)
        if file_paths:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=self.console,
            ) as progress:
                progress.add_task("Loading documents...", total=None)
                task = await self.load_documents(file_paths)
                task.query = query
        
        # Initialize workflow state
        state = WorkflowState(task=task)
        
        # Execute workflow steps
        total_steps = 5
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
        ) as progress:
            # Step 1: Planning
            task_progress = progress.add_task(
                f"[cyan][1/{total_steps}] Planning task...",
                total=None,
            )
            state.current_step = AgentStep.PLANNING
            state.plan = await self.planner.plan(task)
            state.outputs.append(
                AgentOutput(step=AgentStep.PLANNING, content=state.plan)
            )
            progress.update(task_progress, completed=True)
            
            # Step 2: Researching
            progress.update(task_progress, description=f"[cyan][2/{total_steps}] Researching context...")
            state.current_step = AgentStep.RESEARCHING
            state.research_findings = await self.researcher.research(query, state.plan)
            state.outputs.append(
                AgentOutput(step=AgentStep.RESEARCHING, content=state.research_findings)
            )
            
            # Step 3: Analyzing
            progress.update(task_progress, description=f"[cyan][3/{total_steps}] Analyzing findings...")
            state.current_step = AgentStep.ANALYZING
            state.analysis = await self.analyst.analyze(
                query, state.plan, state.research_findings
            )
            state.outputs.append(
                AgentOutput(step=AgentStep.ANALYZING, content=state.analysis)
            )
            
            # Step 4: Critiquing
            progress.update(task_progress, description=f"[cyan][4/{total_steps}] Critiquing analysis...")
            state.current_step = AgentStep.CRITIQUING
            state.critique = await self.critic.critique(query, state.analysis)
            state.outputs.append(
                AgentOutput(step=AgentStep.CRITIQUING, content=state.critique)
            )
            
            # Step 5: Writing
            progress.update(task_progress, description=f"[cyan][5/{total_steps}] Writing final report...")
            state.current_step = AgentStep.WRITING
            state.final_report = await self.writer.write_report(
                query,
                state.plan,
                state.research_findings,
                state.analysis,
                state.critique,
            )
            state.outputs.append(
                AgentOutput(step=AgentStep.WRITING, content=state.final_report)
            )
        
        # Create report
        report = Report(
            task_id=task.id,
            title=query[:100],
            content=state.final_report,
            metadata={
                "steps": len(state.outputs),
                "document_count": len(task.documents),
            },
        )
        
        return report
    
    async def cleanup(self) -> None:
        """Cleanup resources."""
        await self.llm.close()
        await self.vector_store.close()