// # 🔬 LocalResearcherAI
// 
// **Local-first agentic research system that turns your documents into structured reports using local LLMs.**
// 
// [![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
// [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
// [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
// 
// ## ✨ Features
// 
// - **🔒 100% Local** - No API keys required, works completely offline
// - **🤖 Multi-Agent Architecture** - Specialized agents for planning, research, analysis, critique, and writing
// - **📚 RAG Pipeline** - Upload PDFs, Markdown, TXT files for context-aware research
// - **🎯 Production-Ready** - Clean architecture, typed, tested, and containerized
// - **💻 Multiple Interfaces** - CLI, REST API, and Web UI (coming soon)
// - **🧠 Smart Workflow** - Automatic task breakdown and step-by-step execution
// - **📊 Rich Reports** - Generate comprehensive Markdown reports with citations
// 
// ## 🚀 Quick Start
// 
// ### Prerequisites
// 
// 1. **Python 3.12+**
// 2. **Ollama** - [Install Ollama](https://ollama.ai)
// 
// ```bash
// # Install Ollama (macOS/Linux)
// curl -fsSL https://ollama.ai/install.sh | sh
// 
// # Pull recommended models
// ollama pull qwen2.5:latest
// ollama pull nomic-embed-text:latest
// ```
// 
// ### Installation
// 
// ```bash
// # Clone the repository
// git clone https://github.com/yourusername/localresearcher-ai.git
// cd localresearcher-ai
// 
// # Create virtual environment
// python3.12 -m venv venv
// source venv/bin/activate  # On Windows: venv\Scripts\activate
// 
// # Install package
// pip install -e .
// 
// # Or install with dev dependencies
// pip install -e ".[dev]"
// ```
// 
// ### Configuration
// 
// ```bash
// # Copy example env file
// cp .env.example .env
// 
// # Edit .env if needed (defaults work out of the box)
// ```
// 
// ## 💡 Usage
// 
// ### Basic Research
// 
// ```bash
// localresearcher ask "What are the key AI trends in 2024?"
// ```
// 
// ### Analyze Documents
// 
// ```bash
// localresearcher ask "Summarize the key findings" --files examples/sample.md
// ```
// 
// ### Multiple Files
// 
// ```bash
// localresearcher ask "Create an action plan" --files doc1.pdf doc2.md notes.txt
// ```
// 
// ### Custom Output Path
// 
// ```bash
// localresearcher ask "Research topic" --output ./my-report.md
// ```
// 
// ## 🏗️ Architecture
// 
// LocalResearcherAI uses a multi-agent workflow:
// 
// ```
// User Query + Documents
//         ↓
//   [Planner Agent]
//    Creates research plan
//         ↓
//   [Researcher Agent]
//    Gathers information (RAG)
//         ↓
//   [Analyst Agent]
//    Interprets findings
//         ↓
//   [Critic Agent]
//    Evaluates quality
//         ↓
//   [Writer Agent]
//    Generates final report
//         ↓
//   Markdown Report
// ```
// 
// ### Agent Responsibilities
// 
// - **Planner**: Breaks down tasks, identifies research questions
// - **Researcher**: Retrieves relevant context, synthesizes information
// - **Analyst**: Interprets data, extracts insights
// - **Critic**: Evaluates logic, identifies gaps
// - **Writer**: Creates structured, professional reports
// 
// ## 📁 Project Structure
// 
// ```
// localresearcher-ai/
// ├── src/localresearcher/
// │   ├── agents/          # Multi-agent system
// │   │   ├── planner.py
// │   │   ├── researcher.py
// │   │   ├── analyst.py
// │   │   ├── critic.py
// │   │   └── writer.py
// │   ├── core/            # Core abstractions
// │   │   ├── config.py
// │   │   ├── workflow.py
// │   │   ├── schemas.py
// │   │   └── state.py
// │   ├── llm/             # LLM providers
// │   │   ├── base.py
// │   │   └── ollama.py
// │   ├── rag/             # RAG pipeline
// │   │   ├── loader.py
// │   │   ├── chunker.py
// │   │   ├── embeddings.py
// │   │   └── vector_store.py
// │   ├── tools/           # Extensible tools
// │   └── cli/             # CLI interface
// ├── examples/            # Sample documents
// ├── tests/               # Test suite
// └── docs/                # Documentation
// ```
// 
// ## 🛠️ Development
// 
// ### Setup Development Environment
// 
// ```bash
// # Install with dev dependencies
// pip install -e ".[dev]"
// 
// # Install pre-commit hooks
// pre-commit install
// ```
// 
// ### Running Tests
// 
// ```bash
// # Run all tests
// pytest
// 
// # With coverage
// pytest --cov=localresearcher
// ```
// 
// ### Code Quality
// 
// ```bash
// # Format code
// black src/
// 
// # Lint
// ruff check src/
// 
// # Type check
// mypy src/
// ```
// 
// ### Using Makefile
// 
// ```bash
// make install      # Install package
// make test         # Run tests
// make lint         # Run linters
// make format       # Format code
// make clean        # Clean cache files
// ```
// 
// ## 🐳 Docker
// 
// ```bash
// # Build and run with Docker Compose
// docker-compose up
// 
// # Run a query
// docker-compose exec app localresearcher ask "Your question here"
// ```
// 
// ## 🔧 Configuration
// 
// Edit `.env` file:
// 
// ```bash
// # Ollama Configuration
// OLLAMA_BASE_URL=http://localhost:11434
// OLLAMA_MODEL=qwen2.5:latest
// OLLAMA_EMBEDDING_MODEL=nomic-embed-text:latest
// 
// # Database
// DATABASE_PATH=./localresearcher.db
// 
// # Vector Store
// VECTOR_STORE_PATH=./chroma_db
// 
// # Reports
// REPORTS_PATH=./reports
// ```
// 
// ## 🎯 Roadmap
// 
// ### Phase 1 - MVP ✅
// - [x] Multi-agent workflow
// - [x] Ollama integration
// - [x] RAG pipeline
// - [x] CLI interface
// - [x] PDF/Markdown support
// 
// ### Phase 2 - In Progress 🚧
// - [ ] REST API (FastAPI)
// - [ ] Memory system (SQLite)
// - [ ] Tool system (Python runner, calculator)
// - [ ] Streaming responses
// 
// ### Phase 3 - Future 🔮
// - [ ] Web UI (React/Next.js)
// - [ ] Live step visualization in UI
// - [ ] Additional LLM providers (OpenAI, Anthropic)
// - [ ] Advanced tools (web search, git reader)
// - [ ] MCP (Model Context Protocol) support
// 
// ## 🤝 Contributing
// 
// Contributions are welcome! Please:
// 
// 1. Fork the repository
// 2. Create a feature branch (`git checkout -b feature/amazing-feature`)
// 3. Commit your changes (`git commit -m 'Add amazing feature'`)
// 4. Push to the branch (`git push origin feature/amazing-feature`)
// 5. Open a Pull Request
// 
// ## 📄 License
// 
// This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
// 
// ## 🙏 Acknowledgments
// 
// - [Ollama](https://ollama.ai) - Local LLM runtime
// - [ChromaDB](https://www.trychroma.com/) - Vector database
// - [LangChain](https://www.langchain.com/) - Inspiration for agent patterns
// 
// ## 📞 Support
// 
// - **Issues**: [GitHub Issues](https://github.com/yourusername/localresearcher-ai/issues)
// - **Discussions**: [GitHub Discussions](https://github.com/yourusername/localresearcher-ai/discussions)
// 
// ---
// 
// **Built with ❤️ for the local-first AI community**