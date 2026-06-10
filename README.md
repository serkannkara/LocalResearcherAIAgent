// # 🔬 LocalResearcherAI
// 
// <p align="center">
//   <img src="docs/images/architecture.png" alt="LocalResearcherAI Architecture" width="100%">
// </p>
// 
// **Local-first agentic research system that turns your documents into structured reports using local LLMs.**
// 
// [![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
// [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
// [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
// 
// ---
// 
// ## ✨ Features
// 
// - **🔒 100% Local** - No API keys required, works completely offline
// - **🤖 Multi-Agent Architecture** - Specialized agents for planning, research, analysis, critique, and writing
// - **📚 RAG Pipeline** - Upload PDFs, Markdown, TXT files for context-aware research
// - **🎯 Production-Ready** - Clean architecture, typed, tested, and containerized
// - **💻 Multiple Interfaces** - CLI, REST API (coming soon), and Web UI (planned)
// - **🧠 Smart Workflow** - Automatic task breakdown and step-by-step execution
// - **📊 Rich Reports** - Generate comprehensive Markdown reports with citations
// - **🎨 Live Visualization** - Watch agents work in real-time via Rich terminal UI
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
// ### One-Command Install
// 
// **macOS/Linux:**
// ```bash
// git clone https://github.com/yourusername/localresearcher-ai.git
// cd localresearcher-ai
// ./install.sh
// ```
// 
// **Windows:**
// ```bash
// git clone https://github.com/yourusername/localresearcher-ai.git
// cd localresearcher-ai
// install.bat
// ```
// 
// ### Manual Installation
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
// ### Example Output
// 
// ```
// 🔬 LocalResearcherAI
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Query: Analyze AI trends in 2024
// Model: qwen2.5:latest
// Files: 1
// 
// [1/5] Planning task...               ✓
// [2/5] Researching context...         ✓
// [3/5] Analyzing findings...          ✓
// [4/5] Critiquing analysis...         ✓
// [5/5] Writing final report...        ✓
// 
// ✓ Report saved to: reports/report_abc123.md
// ```
// 
// ## 🏗️ Architecture
// 
// LocalResearcherAI uses a multi-agent workflow where specialized agents collaborate:
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
// | Agent | Responsibility | Output |
// |-------|---------------|--------|
// | **Planner** | Breaks down tasks, identifies research questions | Research plan |
// | **Researcher** | Retrieves relevant context, synthesizes information | Research findings |
// | **Analyst** | Interprets data, extracts insights | Analysis report |
// | **Critic** | Evaluates logic, identifies gaps | Critical review |
// | **Writer** | Creates structured, professional reports | Final Markdown report |
// 
// For detailed architecture, see [ARCHITECTURE.md](docs/ARCHITECTURE.md)
// 
// ## 📁 Project Structure
// 
// ```
// localresearcher-ai/
// ├── src/localresearcher/
// │   ├── agents/          # 5 specialized agents
// │   ├── core/            # Core abstractions & workflow
// │   ├── llm/             # LLM providers (Ollama, etc.)
// │   ├── rag/             # RAG pipeline (load, chunk, embed, retrieve)
// │   ├── tools/           # Extensible tool system
// │   ├── memory/          # Memory & state management
// │   └── cli/             # CLI interface
// ├── examples/            # Sample documents
// ├── tests/               # Test suite
// ├── docs/                # Documentation
// ├── Dockerfile           # Docker support
// └── pyproject.toml       # Package configuration
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
// 
// # Run specific test
// pytest tests/test_basic.py
// ```
// 
// ### Code Quality
// 
// ```bash
// # Format code
// black src/ tests/
// 
// # Lint
// ruff check src/ tests/
// 
// # Type check
// mypy src/
// 
// # Run all checks
// make lint
// ```
// 
// ### Using Makefile
// 
// ```bash
// make install      # Install package
// make install-dev  # Install with dev dependencies
// make test         # Run tests
// make test-cov     # Run tests with coverage
// make lint         # Run linters
// make format       # Format code
// make clean        # Clean cache files
// make run          # Run example query
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
// Edit `.env` file (copy from `.env.example`):
// 
// ```bash
// # Ollama Configuration
// OLLAMA_BASE_URL=http://localhost:11434
// OLLAMA_MODEL=qwen2.5:latest
// OLLAMA_EMBEDDING_MODEL=nomic-embed-text:latest
// 
// # Database & Storage
// DATABASE_PATH=./localresearcher.db
// VECTOR_STORE_PATH=./chroma_db
// REPORTS_PATH=./reports
// 
// # RAG Settings
// CHUNK_SIZE=1000
// CHUNK_OVERLAP=200
// TOP_K_RETRIEVAL=5
// ```
// 
// ## 🎯 Roadmap
// 
// ### Phase 1 - MVP ✅ (Current)
// - [x] Multi-agent workflow
// - [x] Ollama integration
// - [x] RAG pipeline with ChromaDB
// - [x] CLI interface with Rich visualization
// - [x] PDF/Markdown/TXT support
// - [x] Docker deployment
// 
// ### Phase 2 - Enhanced Capabilities 🚧 (In Progress)
// - [ ] REST API (FastAPI)
// - [ ] Memory system (SQLite)
// - [ ] Tool expansion (Python runner, calculator)
// - [ ] Streaming responses
// - [ ] DOCX, CSV, JSON support
// 
// ### Phase 3 - Web Interface 🔮 (Planned)
// - [ ] Modern Web UI (React/Next.js)
// - [ ] Live agent step visualization
// - [ ] Workflow builder
// - [ ] Batch processing
// - [ ] Export to PDF/JSON
// 
// ### Phase 4 - Advanced Features 🌟 (Future)
// - [ ] Multi-modal support (images, OCR)
// - [ ] Web search integration (optional)
// - [ ] Git repository analysis
// - [ ] MCP (Model Context Protocol) support
// - [ ] Custom agent creation
// 
// ## 📖 Documentation
// 
// - [Quick Start Guide](docs/QUICKSTART.md) - Step-by-step setup
// - [Architecture](docs/ARCHITECTURE.md) - Technical deep dive
// - [Vision](VISION.md) - Project philosophy and goals
// - [Contributing](CONTRIBUTING.md) - How to contribute
// - [Project Summary](docs/PROJECT_SUMMARY.md) - Overview and stats
// 
// ## 🤝 Contributing
// 
// Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
// 
// Ways to contribute:
// - 🐛 Report bugs
// - 💡 Suggest features
// - 📝 Improve documentation
// - 🔧 Submit pull requests
// - ⭐ Star the project
// 
// ## 📊 Tech Stack
// 
// **Core:**
// - Python 3.12+ with full type hints
// - Pydantic for data validation
// - AsyncIO for concurrent operations
// 
// **LLM & RAG:**
// - Ollama (local LLM runtime)
// - ChromaDB (vector database)
// - nomic-embed-text (embeddings)
// 
// **CLI & Visualization:**
// - Typer (CLI framework)
// - Rich (terminal UI)
// 
// **Development:**
// - Pytest (testing)
// - Ruff (linting)
// - Black (formatting)
// - MyPy (type checking)
// - Pre-commit hooks
// 
// ## 🌟 Why LocalResearcherAI?
// 
// ### Privacy First
// - Your data never leaves your computer
// - No cloud dependencies
// - Perfect for sensitive documents
// 
// ### Cost Effective
// - No per-token charges
// - No monthly subscriptions
// - Run unlimited queries
// 
// ### Transparent
// - See every agent step
// - Understand AI reasoning
// - Debuggable workflow
// 
// ### Extensible
// - Add custom agents
// - Create new tools
// - Modify prompts
// - Plugin architecture
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
// - Open source community
// 
// ## 📞 Support
// 
// - **Issues**: [GitHub Issues](https://github.com/yourusername/localresearcher-ai/issues)
// - **Discussions**: [GitHub Discussions](https://github.com/yourusername/localresearcher-ai/discussions)
// - **Documentation**: [docs/](docs/)
// 
// ## ⭐ Star History
// 
// If you find this project useful, please consider giving it a star!
// 
// ---
// 
// <p align="center">
//   <strong>Built with ❤️ for the local-first AI community</strong>
// </p>
// 
// <p align="center">
//   <a href="#-quick-start">Get Started</a> •
//   <a href="docs/QUICKSTART.md">Documentation</a> •
//   <a href="CONTRIBUTING.md">Contribute</a>
// </p>