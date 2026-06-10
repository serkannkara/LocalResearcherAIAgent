"""Planner agent - breaks down tasks into steps."""

from localresearcher.llm.base import BaseLLMProvider
from localresearcher.core.schemas import Task


class PlannerAgent:
    """Agent responsible for task planning and breakdown."""
    
    def __init__(self, llm: BaseLLMProvider):
        self.llm = llm
    
    async def plan(self, task: Task) -> str:
        """Create a research plan for the given task."""
        system_prompt = """You are an expert research planner. Your job is to break down research tasks into clear, actionable steps.

Create a structured plan that:
1. Identifies key research questions
2. Determines what information is needed
3. Outlines analysis approach
4. Defines success criteria

Be concise and specific."""
        
        documents_context = ""
        if task.documents:
            doc_list = "\n".join([f"- {doc.path}" for doc in task.documents])
            documents_context = f"\n\nAvailable documents:\n{doc_list}"
        
        prompt = f"""Task: {task.query}{documents_context}

Create a detailed research plan for this task."""
        
        plan = await self.llm.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.7,
            max_tokens=1000,
        )
        
        return plan