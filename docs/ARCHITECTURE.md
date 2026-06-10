// # Architecture Documentation
// 
// ## Overview
// 
// LocalResearcherAI is built on a multi-agent architecture where specialized agents collaborate to produce research reports.
// 
// ## Core Principles
// 
// 1. **Single Responsibility** - Each agent has one clear purpose
// 2. **Local-First** - No external API dependencies required
// 3. **Extensible** - Easy to add new agents and tools
// 4. **Type-Safe** - Full type hints and Pydantic models
// 5. **Testable** - Dependency injection and clean interfaces
// 
// ## System Components
// 
// ### 1. LLM Layer (`src/localresearcher/llm/`)
// 
// **Base Interface**: `BaseLLMProvider`
// - Defines contract for all LLM providers
// - Async-first API
// - Supports streaming
// 
// **Implementations**:
// - `OllamaProvider` - Local Ollama integration
// - Future: OpenAI, Anthropic, etc.
// 
// ### 2. RAG Pipeline (`src/localresearcher/rag/`)
// 
// **Document Loading** (`loader.py`):
// - Protocol-based loader system
// - Supports PDF, Markdown, TXT
// - Extensible for new formats
// 
// **Chunking** (`chunker.py`):
// - Overlap-based text splitting
// - Sentence boundary awareness
// - Configurable chunk size
// 
// **Embeddings** (`embeddings.py`):
// - Local embedding via Ollama
// - Batch processing support
// - Uses nomic-embed-text by default
// 
// **Vector Store** (`vector_store.py`):
// - ChromaDB integration
// - Persistent storage
// - Cosine similarity search
// 
// ### 3. Agent System (`src/localresearcher/agents/`)
// 
// Each agent is independent and focused:
// 
// **PlannerAgent**:
// - Input: Task query + available documents
// - Output: Structured research plan
// - Responsibility: Break down complex tasks
// 
// **ResearcherAgent**:
// - Input: Query + plan
// - Output: Research findings
// - Responsibility: Gather relevant information via RAG
// 
// **AnalystAgent**:
// - Input: Query + plan + findings
// - Output: Analysis and insights
// - Responsibility: Interpret data and draw conclusions
// 
// **CriticAgent**:
// - Input: Query + analysis
// - Output: Critical evaluation
// - Responsibility: Identify gaps and weaknesses
// 
// **WriterAgent**:
// - Input: All previous outputs
// - Output: Final structured report
// - Responsibility: Create professional documentation
// 
// ### 4. Workflow Orchestration (`src/localresearcher/core/workflow.py`)
// 
// **ResearchWorkflow**:
// - Coordinates agent execution
// - Manages state between steps
// - Handles errors and retries
// - Provides progress feedback
// 
// **Execution Flow**:
// ```
// 1. Load documents → Vector store
// 2. PlannerAgent → Create plan
// 3. ResearcherAgent → Gather info (uses vector store)
// 4. AnalystAgent → Analyze findings
// 5. CriticAgent → Evaluate quality
// 6. WriterAgent → Generate report
// ```
// 
// ### 5. Data Models (`src/localresearcher/core/schemas.py`)
// 
// All data structures use Pydantic for validation:
// 
// - `Document`: File metadata and content
// - `Task`: Research task definition
// - `WorkflowState`: Execution state tracking
// - `AgentOutput`: Individual agent results
// - `Report`: Final output structure
// 
// ### 6. Configuration (`src/localresearcher/core/config.py`)
// 
// - Pydantic Settings for env management
// - Type-safe configuration
// - Automatic directory creation
// - Validation on load
// 
// ## Data Flow
// 
// ```
// User Input (Query + Files)
//         ↓
// DocumentLoader
//         ↓
// TextChunker
//         ↓
// EmbeddingProvider
//         ↓
// VectorStore (ChromaDB)
//         ↓
// ┌─────────────────┐
// │ WorkflowState   │
// │  - Task         │
// │  - Documents    │
// │  - Current Step │
// └─────────────────┘
//         ↓
// ┌─────────────────┐
// │ Agent Pipeline  │
// │  1. Planner     │
// │  2. Researcher  │ ← Queries VectorStore
// │  3. Analyst     │
// │  4. Critic      │
// │  5. Writer      │
// └─────────────────┘
//         ↓
// Report (Markdown)
// ```
// 
// ## Extension Points
// 
// ### Adding a New Agent
// 
// 1. Create agent class in `agents/`
// 2. Inject LLM provider
// 3. Implement async method
// 4. Add to workflow execution
// 
// ### Adding a New Tool
// 
// 1. Create tool class in `tools/`
// 2. Define execution interface
// 3. Register in tool system
// 4. Use in agent prompts
// 
// ### Adding a New LLM Provider
// 
// 1. Inherit from `BaseLLMProvider`
// 2. Implement required methods
// 3. Add configuration options
// 4. Test availability check
// 
// ## Performance Considerations
// 
// - **Async by default**: All I/O operations are async
// - **Batch embeddings**: Multiple documents processed together
// - **Chunking strategy**: Configurable for memory/quality tradeoff
// - **Vector store**: Persistent to avoid re-embedding
// 
// ## Testing Strategy
// 
// - Unit tests for individual components
// - Integration tests for workflows
// - Mock LLM responses for deterministic tests
// - Test fixtures for sample documents
// 
// ## Security
// 
// - No API keys required by default
// - Local execution only
// - No data leaves the machine
// - Optional API providers clearly marked