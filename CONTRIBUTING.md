// # Contributing to LocalResearcherAI
// 
// Thank you for your interest in contributing! 🎉
// 
// ## Getting Started
// 
// ### 1. Fork and Clone
// 
// ```bash
// git clone https://github.com/yourusername/localresearcher-ai.git
// cd localresearcher-ai
// ```
// 
// ### 2. Setup Development Environment
// 
// ```bash
// python3.12 -m venv venv
// source venv/bin/activate
// make install-dev
// ```
// 
// ### 3. Create a Branch
// 
// ```bash
// git checkout -b feature/your-feature-name
// ```
// 
// ## Development Workflow
// 
// ### Running Tests
// 
// ```bash
// make test
// make test-cov  # With coverage report
// ```
// 
// ### Code Quality
// 
// ```bash
// make format  # Format code
// make lint    # Check linting
// ```
// 
// ### Before Committing
// 
// - Run tests
// - Run linters
// - Update documentation if needed
// - Add type hints to new code
// 
// ## Pull Request Process
// 
// 1. Update README.md if needed
// 2. Add tests for new features
// 3. Ensure all tests pass
// 4. Update CHANGELOG.md
// 5. Submit PR with clear description
// 
// ## Code Style
// 
// - Python 3.12+ features
// - Type hints everywhere
// - Black for formatting
// - Ruff for linting
// - Docstrings for public APIs
// 
// ## Adding New Features
// 
// ### New Agent
// 
// Create `src/localresearcher/agents/your_agent.py`:
// 
// ```python
// from localresearcher.llm.base import BaseLLMProvider
// 
// class YourAgent:
//     def __init__(self, llm: BaseLLMProvider):
//         self.llm = llm
//     
//     async def execute(self, input: str) -> str:
//         # Implementation
//         pass
// ```
// 
// ### New Tool
// 
// Create `src/localresearcher/tools/your_tool.py`:
// 
// ```python
// class YourTool:
//     async def execute(self, **kwargs: Any) -> dict[str, Any]:
//         # Implementation
//         pass
// ```
// 
// ### New LLM Provider
// 
// Create `src/localresearcher/llm/your_provider.py`:
// 
// ```python
// from localresearcher.llm.base import BaseLLMProvider
// 
// class YourProvider(BaseLLMProvider):
//     async def generate(self, prompt: str, **kwargs) -> str:
//         # Implementation
//         pass
// ```
// 
// ## Questions?
// 
// Open an issue or start a discussion!