<div align="center">

# 🔬 LocalResearcherAI
 
### Don't just ask AI. **Understand why it answered.**

**Private by default. Transparent by design. Powered by local LLMs.**

[![Python Version](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Local First](https://img.shields.io/badge/Local--First-100%25-22c55e?style=for-the-badge)](https://github.com/serkannkara/LocalResearcherAI)
[![Ollama Ready](https://img.shields.io/badge/Ollama-Ready-000000?style=for-the-badge&logo=ollama)](https://ollama.ai)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/linter-ruff-blueviolet?style=for-the-badge)](https://github.com/astral-sh/ruff)

[Features](#-key-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [Documentation](#-documentation) • [Roadmap](#-roadmap)

<img src="architecture.png" alt="LocalResearcherAI Architecture" width="100%">

</div>

---

## 🎯 What is LocalResearcherAI?
 
**LocalResearcherAI** is a **local-first, multi-agent AI research assistant** that analyzes documents on your machine using **100% local LLMs**. No cloud. No API keys. No data exfiltration.

### The Core Principle

> **Every answer should make clear what it is based on.**

Traditional AI tools give you answers. LocalResearcherAI gives you **verifiable research**.

| Traditional AI | LocalResearcherAI |
|----------------|-------------------|
| "Here's an answer" | "Here's an answer **based on...**" |
| Unknown sources | Clear evidence trail |
| Cloud-dependent | 100% local execution |
| Black box reasoning | Transparent agent pipeline |
| Privacy concerns | Your data never leaves your machine |

---

## ✨ Key Features
 
### 🔐 Privacy & Control

- **100% Local Execution**: Runs entirely on your machine via [Ollama](https://ollama.ai)
- **No Cloud Dependencies**: Zero API calls, zero tracking, zero data leaks
- **Air-Gap Compatible**: Works offline after initial model download
- **Your Data Stays Yours**: Documents never leave your computer

### 🧠 Intelligent Modes

LocalResearcherAI automatically switches between two distinct modes:

#### 🧾 Knowledge Mode

Used when **no documents** are provided.

```bash
localresearcher ask "Explain quantum entanglement"
```

**Output characteristics:**
- Clearly labeled as "unverified knowledge"
- Based on model's training data
- No external evidence claims
- Fast, exploratory answers

#### 🔬 Evidence Mode

Activated when **documents** are provided.

```bash
localresearcher ask "Summarize key findings" --files research.pdf
```

**Output characteristics:**
- Document-backed analysis
- RAG-powered retrieval
- Evidence-based conclusions
- Transparent sourcing

### 🤖 Multi-Agent Architecture

Built on a **5-agent pipeline** for comprehensive research:

| Agent | Role | Responsibility |
|-------|------|----------------|
| **🎯 Intent Classifier** | Router | Detects greetings, small talk, or research queries |
| **📋 Planner** | Strategist | Breaks queries into structured research plans |
| **🔍 Researcher** | Gatherer | Retrieves information from documents or model knowledge |
| **🧪 Analyst** | Synthesizer | Identifies patterns, connections, and insights |
| **🔎 Critic** | Reviewer | Evaluates gaps, weaknesses, and missing perspectives |
| **✍️ Writer** | Reporter | Generates final markdown reports |

### 📄 Document Support

Natively supports multiple formats:

- ✅ **PDF** (via `pypdf`)
- ✅ **Markdown** (`.md`)
- ✅ **Plain Text** (`.txt`)
- ✅ **Word Documents** (`.docx`, via `python-docx`)
- ✅ **Glob Patterns** (`./docs/**/*.pdf`)

### 🚀 Developer-Friendly

- **Modern Python 3.12+** with full type hints
- **Async/await** throughout for performance
- **Structured logging** via `rich`
- **Comprehensive error handling** with retry logic
- **CLI built with Typer** for excellent UX
- **Vector storage** via ChromaDB
- **Pre-commit hooks** for code quality
- **Testing ready** with pytest

---

## 🚀 Quick Start
 
### Prerequisites

1. **Python 3.12+** installed
2. **Ollama** installed and running ([Download here](https://ollama.ai))

### Installation

#### Option 1: Automated Install (Recommended)

```bash
git clone https://github.com/serkannkara/LocalResearcherAI.git
cd LocalResearcherAI
./install.sh  # On Unix/macOS
# OR
install.bat   # On Windows
```

#### Option 2: Manual Install

```bash
git clone https://github.com/serkannkara/LocalResearcherAI.git
cd LocalResearcherAI

# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package
pip install -e .
```

### Download Models

LocalResearcherAI requires two models:

```bash
# Main LLM (default: qwen2.5, ~4GB)
ollama pull qwen2.5:latest

# Embeddings model (~274MB)
ollama pull nomic-embed-text:latest
```

**Alternative models:**

```bash
# Smaller, faster (good for testing)
ollama pull qwen2.5:0.5b

# Larger, more capable
ollama pull qwen2.5:7b
ollama pull llama3.1:8b
```

To use a different model, set it in `.env`:

```bash
cp .env.example .env
# Edit .env and set OLLAMA_MODEL=your-preferred-model
```

### Verify Installation

```bash
localresearcher ask "Hello, are you working?"
```

You should see:

```
🔬 LocalResearcherAI

Query: Hello, are you working?
Model: qwen2.5:latest
Files: 0

🧠 Detecting intent...
✓ Greeting detected

👋 Hello! Yes, I'm working perfectly...
```

---

## 📖 Usage Examples
 
### Basic Research Query

```bash
localresearcher ask "What is Agentic AI?"
```

**Output:**
```
🧠 Knowledge Mode

No documents provided.
No web search available.
No external evidence.

This is an AI-generated explanation, not verified research.
For verifiable results, provide documents.

✓ Report saved to: reports/report_<uuid>.md
```

### Analyze a Single Document

```bash
localresearcher ask "Summarize the main findings" --files report.pdf
```

### Compare Multiple Documents

```bash
localresearcher ask "Compare Q1 and Q2 performance" \
  --files Q1-report.pdf \
  --files Q2-report.pdf
```

### Analyze All Files in a Directory

```bash
localresearcher ask "Identify common themes across all research papers" \
  --files "./papers/**/*.pdf"
```

### Save Output to Custom Location

```bash
localresearcher ask "Analyze market trends" \
  --files market-data.pdf \
  --output ./analysis/market-trends.md
```

### Real-World Use Cases

#### 📚 Academic Research

```bash
localresearcher ask "Summarize methodology across these papers" \
  --files paper1.pdf --files paper2.pdf --files paper3.pdf
```

#### 💼 Business Analysis

```bash
localresearcher ask "Analyze quarterly financial performance" \
  --files Q4-2024-report.pdf
```

#### ⚖️ Legal Review

```bash
localresearcher ask "Identify potential risks and liabilities" \
  --files contract.docx
```

#### 🧠 Personal Knowledge Management

```bash
localresearcher ask "Summarize my notes from this week" \
  --files "./notes/2024-06-*.md"
```

---

## 🏗️ Architecture
 
### System Overview

```
┌─────────────────────────────────────────────────────────┐
│                      User Query                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              🧠 Intent Classifier                        │
│   (Greeting | Small Talk | Research)                    │
└──────────────┬─────────────────────┬────────────────────┘
               │                     │
      Greeting/│                     │Research
      SmallTalk│                     │
               ▼                     ▼
   ┌────────────────┐   ┌───────────────────────────────┐
   │ Quick Response │   │   📋 Multi-Agent Pipeline     │
   └────────────────┘   └───────────┬───────────────────┘
                                    │
                        ┌───────────┴──────────┐
                        │   Workflow Manager   │
                        └───────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
       ┌──────────┐          ┌──────────┐          ┌──────────┐
       │ Planner  │  ───►    │Researcher│  ───►    │ Analyst  │
       └──────────┘          └────┬─────┘          └──────────┘
                                  │                      │
                                  │                      ▼
                                  │                ┌──────────┐
                                  │                │  Critic  │
                                  │                └────┬─────┘
                                  │                     │
                                  ▼                     ▼
                           ┌─────────────┐       ┌──────────┐
                           │  RAG Layer  │       │  Writer  │
                           │             │       └────┬─────┘
                           │ ┌─────────┐ │            │
                           │ │Documents│ │            ▼
                           │ └─────────┘ │    ┌───────────────┐
                           │ ┌─────────┐ │    │ Markdown      │
                           │ │ Chunker │ │    │ Report        │
                           │ └─────────┘ │    └───────────────┘
                           │ ┌─────────┐ │
                           │ │Embedding│ │
                           │ └─────────┘ │
                           │ ┌─────────┐ │
                           │ │ Vector  │ │
                           │ │  Store  │ │
                           │ │(Chroma) │ │
                           │ └─────────┘ │
                           └──────┬──────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Ollama (Local)  │
                         │   qwen2.5       │
                         │ nomic-embed-text│
                         └─────────────────┘
```

### Workflow State Management

LocalResearcherAI maintains a **single source of truth** throughout execution:

```
WorkflowState
├─ task_id: UUID
├─ query: str
├─ documents: List[Document]
├─ current_step: AgentStep
├─ agent_outputs:
│  ├─ planner_output: PlannerOutput
│  ├─ research_findings: List[Finding]
│  ├─ analysis: AnalysisOutput
│  ├─ critique: CritiqueOutput
│  └─ final_report: Report
└─ metadata:
   ├─ intent_type: IntentType
   ├─ confidence: float
   ├─ has_external_evidence: bool
   ├─ research_performed: bool
   ├─ document_count: int
   ├─ chunk_count: int
   └─ timestamp: datetime
```

## 📊 Performance
 
Benchmarks on **Apple M1 Pro** (10-core CPU, 16GB RAM):

| Task | Typical Time | Model Used |
|------|--------------|------------|
| **Intent Detection** | 200-500ms | qwen2.5:latest |
| **Document Loading** (100-page PDF) | 1-2s | - |
| **Chunking + Embedding** (100 pages) | 3-5s | nomic-embed-text |
| **Vector Retrieval** (top 5 chunks) | 50-300ms | ChromaDB |
| **Single Agent Step** | 2-8s | qwen2.5:latest |
| **Full 5-Agent Pipeline** | 15-45s | qwen2.5:latest |

**Performance Tips:**

- Use **smaller models** for faster responses: `qwen2.5:0.5b`
- Enable **GPU acceleration** if available (CUDA/Metal)
- Increase **chunk size** for fewer, faster retrievals
- Use **caching** for repeated queries on same documents

---

## 🗂️ Project Structure
 
```
LocalResearcherAI/
├── src/
│   └── localresearcher/
│       ├── agents/               # Multi-agent system
│       │   ├── intent_classifier.py
│       │   ├── planner.py
│       │   ├── researcher.py
│       │   ├── analyst.py
│       │   ├── critic.py
│       │   └── writer.py
│       ├── cli/                  # Command-line interface
│       │   └── main.py
│       ├── core/                 # Core logic
│       │   ├── config.py
│       │   ├── intent.py
│       │   ├── logging.py
│       │   ├── retry.py
│       │   ├── schemas.py
│       │   └── workflow.py
│       ├── llm/                  # LLM providers
│       │   ├── base.py
│       │   └── ollama.py
│       ├── rag/                  # RAG components
│       │   ├── chunker.py
│       │   ├── embeddings.py
│       │   ├── loader.py
│       │   └── vector_store.py
│       ├── memory/               # (Future) Memory system
│       └── tools/                # Utility tools
│           └── file_reader.py
├── tests/                        # Test suite
│   ├── test_basic.py
│   └── __init__.py
├── reports/                      # Generated reports
├── chroma_db/                    # Vector store data
├── logs/                         # Application logs
├── .github/                      # GitHub workflows
├── architecture.png              # Architecture diagram
├── pyproject.toml                # Project metadata
├── .env.example                  # Environment template
├── install.sh                    # Unix installer
├── install.bat                   # Windows installer
├── Dockerfile                    # Container image
├── docker-compose.yml            # Docker setup
├── Makefile                      # Build commands
└── README.md                     # This file
```

**Total:** ~2,080 lines of Python code

---

## 🛠️ Development
 
### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/serkannkara/LocalResearcherAI.git
cd LocalResearcherAI

# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=localresearcher --cov-report=html

# Run specific test
pytest tests/test_basic.py -v
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/

# Run all checks (pre-commit)
pre-commit run --all-files
```

### Docker Development

```bash
# Build image
docker build -t localresearcher:dev .

# Run container
docker-compose up -d

# Execute query
docker exec -it localresearcher localresearcher ask "Test query"
```

### Makefile Commands

```bash
make install      # Install package
make test         # Run tests
make lint         # Run linters
make format       # Format code
make clean        # Clean artifacts
make docker       # Build Docker image
```

---

## 🤝 Contributing
 
Contributions are **highly welcome**! Here's how:

### Ways to Contribute

1. 🐛 **Report Bugs**: [Open an issue](https://github.com/serkannkara/LocalResearcherAI/issues/new?template=bug_report.md)
2. 💡 **Suggest Features**: [Open a discussion](https://github.com/serkannkara/LocalResearcherAI/discussions/new)
3. 📖 **Improve Docs**: Fix typos, add examples, write guides
4. 🧪 **Write Tests**: Increase coverage, add edge cases
5. 🔧 **Fix Issues**: Check [good first issues](https://github.com/serkannkara/LocalResearcherAI/labels/good%20first%20issue)
6. ✨ **Add Features**: Implement items from roadmap

### Contribution Workflow

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Test** your changes (`pytest`)
5. **Commit** with conventional commits (`git commit -m 'feat: add amazing feature'`)
6. **Push** to your fork (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

### Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding/updating tests
- `chore`: Maintenance tasks

**Examples:**

```bash
feat(rag): add support for DOCX files
fix(agents): resolve planner timeout issue
docs(readme): update installation instructions
```

### Good First Issues

Looking to contribute? Start here:

- [ ] Add support for `.epub` files
- [ ] Improve error messages for common issues
- [ ] Add progress bars for long-running operations
- [ ] Write tutorial for academic research use case
- [ ] Add integration tests for full workflows
- [ ] Create example scripts for common tasks
- [ ] Improve logging with structured context
- [ ] Add configuration validation

---

## ❓ FAQ
 
### General Questions

**Q: Is this really 100% local?**  
A: Yes! Once models are downloaded, no internet connection is required. All processing happens on your machine.

**Q: Do I need a GPU?**  
A: No, but it helps. Ollama works on CPU (slower) or GPU (faster). M1/M2 Macs use Metal acceleration automatically.

**Q: How much RAM do I need?**  
A: Minimum 8GB. Recommended 16GB+ for larger models and documents.

**Q: Can I use OpenAI/Anthropic instead of Ollama?**  
A: Not currently, but it's on the roadmap! For now, LocalResearcherAI is local-only by design.

**Q: How does this compare to ChatGPT?**  
A: ChatGPT is cloud-based and general-purpose. LocalResearcherAI is local, privacy-focused, and designed specifically for document-backed research with transparent reasoning.

### Technical Questions

**Q: Which model should I use?**  
A: Start with `qwen2.5:latest` (4GB). For better quality, try `qwen2.5:7b` or `llama3.1:8b`. For speed, use `qwen2.5:0.5b`.

**Q: Can I use custom models?**  
A: Yes! Any model available in Ollama works. Set `OLLAMA_MODEL=your-model` in `.env`.

**Q: How do I speed up processing?**  
A: Use smaller models, enable GPU acceleration, increase chunk size, or run Ollama on a dedicated machine.

**Q: Where are reports saved?**  
A: By default in `./reports/`. Use `--output` flag to specify custom location.

**Q: Can I process multiple PDFs at once?**  
A: Yes! Use multiple `--files` flags or glob patterns: `--files "./docs/*.pdf"`.

**Q: Does it support other languages?**  
A: Yes! Qwen 2.5 supports many languages. Results depend on the model's training data.

### Troubleshooting

**Q: "Ollama is not available" error**  
A: 
1. Check Ollama is running: `ollama list`
2. Verify model is installed: `ollama pull qwen2.5:latest`
3. Test Ollama directly: `ollama run qwen2.5:latest "Hello"`

**Q: "File not found" error**  
A: Check file path is correct and file exists. Use absolute paths if relative paths don't work.

**Q: Slow performance**  
A:
1. Use a smaller model: `qwen2.5:0.5b`
2. Enable GPU acceleration (check Ollama docs)
3. Reduce document size or chunk count
4. Close other applications to free RAM

**Q: ChromaDB errors**  
A: Delete `./chroma_db/` folder and restart. Vector store will rebuild automatically.

**Q: Module not found errors**  
A: Reinstall package: `pip install -e .` or check virtual environment is activated.

---

## 🔗 Related Projects
 
### Similar Tools

- [LangChain](https://github.com/langchain-ai/langchain) - Framework for LLM applications (more general)
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for LLMs (focuses on indexing)
- [PrivateGPT](https://github.com/imartinez/privateGPT) - Local document QA (simpler, single-agent)
- [LocalGPT](https://github.com/PromtEngineer/localGPT) - Another local document QA tool

### Complementary Tools

- [Ollama](https://ollama.ai) - Local LLM inference engine
- [ChromaDB](https://www.trychroma.com) - Vector database
- [Obsidian](https://obsidian.md) - Note-taking (great for storing reports)
- [Zotero](https://www.zotero.org) - Reference management

### Comparisons

| Feature | LocalResearcherAI | PrivateGPT | LangChain | ChatGPT |
|---------|-------------------|------------|-----------|---------|
| **Local Execution** | ✅ 100% | ✅ 100% | ⚠️ Optional | ❌ Cloud only |
| **Multi-Agent** | ✅ 5 agents | ❌ Single | ⚠️ Manual | ❌ N/A |
| **Transparent Reasoning** | ✅ Full trail | ⚠️ Limited | ⚠️ Depends | ❌ Black box |
| **Intent Detection** | ✅ Built-in | ❌ No | ❌ No | ⚠️ Implicit |
| **Evidence Attribution** | 🚧 Phase 2 | ⚠️ Basic | ⚠️ Manual | ❌ No |
| **Developer-Friendly** | ✅ Type hints | ⚠️ Limited | ✅ Yes | N/A |

---

## 📜 License
 
**MIT License** - See [LICENSE](LICENSE) for details.

You are free to:
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Use privately

---

## 🙏 Acknowledgments
 
Built with ❤️ using these amazing open-source projects:

- **[Ollama](https://ollama.ai)** - Making local LLMs accessible to everyone
- **[ChromaDB](https://www.trychroma.com)** - The AI-native open-source embedding database
- **[Typer](https://typer.tiangolo.com)** - Modern CLI framework by Sebastián Ramírez
- **[Rich](https://rich.readthedocs.io)** - Beautiful terminal formatting by Will McGugan
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation using Python type hints
- **[Qwen Team](https://github.com/QwenLM)** - Powerful open-source language models

### Citations

If you use LocalResearcherAI in academic work, please cite:

```bibtex
@software{localresearcherai2024,
  author = {Kara, Serkan},
  title = {LocalResearcherAI: Local-First Multi-Agent Research Assistant},
  year = {2024},
  url = {https://github.com/serkannkara/LocalResearcherAI},
  note = {Open-source agentic research system using local LLMs}
}
```

### Special Thanks

- **Ollama Community** for making local AI practical
- **LangChain Team** for pioneering agent architectures
 - **Anthropic** for advancing interpretable AI research
 - **Early testers** for valuable feedback
 
 ---
 
 ## 📞 Contact & Support
 
 - **Issues**: [GitHub Issues](https://github.com/serkannkara/LocalResearcherAI/issues)
 - **Discussions**: [GitHub Discussions](https://github.com/serkannkara/LocalResearcherAI/discussions)
 - **Email**: serkankara@example.com
 - **Twitter**: [@serkannkara](https://twitter.com/serkannkara)
 
 ---
 
 <div align="center">
 
 **Made with ❤️ by [Serkan Kara](https://github.com/serkannkara)**
 
 ⭐ **Star this repo** if you find it useful!
 
 [Report Bug](https://github.com/serkannkara/LocalResearcherAI/issues/new?template=bug_report.md) • [Request Feature](https://github.com/serkannkara/LocalResearcherAI/issues/new?template=feature_request.md) • [Documentation](https://github.com/serkannkara/LocalResearcherAI/wiki)
 
 </div>
