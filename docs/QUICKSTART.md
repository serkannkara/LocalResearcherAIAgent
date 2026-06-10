// # Quick Start Guide
// 
// This guide will get you up and running with LocalResearcherAI in 5 minutes.
// 
// ## Step 1: Prerequisites
// 
// ### Install Python 3.12+
// 
// ```bash
// # Check your Python version
// python3 --version
// 
// # Should be 3.12 or higher
// ```
// 
// ### Install Ollama
// 
// **macOS/Linux:**
// ```bash
// curl -fsSL https://ollama.ai/install.sh | sh
// ```
// 
// **Windows:**
// Download from [ollama.ai](https://ollama.ai)
// 
// ### Pull Models
// 
// ```bash
// # Main LLM (choose one)
// ollama pull qwen2.5:latest      # Recommended, 4.7GB
// # OR
// ollama pull llama3.1:latest     # Alternative, 4.7GB
// 
// # Embedding model (required)
// ollama pull nomic-embed-text:latest  # 274MB
// ```
// 
// **Verify models:**
// ```bash
// ollama list
// ```
// 
// ## Step 2: Install LocalResearcherAI
// 
// ```bash
// # Clone the repository
// git clone https://github.com/yourusername/localresearcher-ai.git
// cd localresearcher-ai
// 
// # Create and activate virtual environment
// python3 -m venv venv
// source venv/bin/activate  # On Windows: venv\Scripts\activate
// 
// # Install the package
// pip install -e .
// ```
// 
// ## Step 3: Configure (Optional)
// 
// ```bash
// # Copy environment template
// cp .env.example .env
// 
// # Edit if needed (defaults work for most users)
// # nano .env
// ```
// 
// ## Step 4: Test Installation
// 
// ```bash
// # Check version
// localresearcher version
// 
// # Should display version info and model configuration
// ```
// 
// ## Step 5: Run Your First Query
// 
// ### Simple Question
// 
// ```bash
// localresearcher ask "What are the key benefits of local-first AI systems?"
// ```
// 
// ### Analyze a Document
// 
// ```bash
// localresearcher ask "Summarize the key points" --files examples/sample.md
// ```
// 
// ### Expected Output
// 
// You should see:
// 1. Progress indicators for each agent step
// 2. Final report in terminal
// 3. Saved report in `./reports/` directory
// 
// ## Step 6: View the Report
// 
// ```bash
// # Reports are saved as Markdown
// ls reports/
// 
// # View the latest report
// cat reports/report_*.md
// ```
// 
// ## Troubleshooting
// 
// ### "Ollama is not available"
// 
// ```bash
// # Check if Ollama is running
// ollama list
// 
// # If not, start Ollama
// ollama serve
// ```
// 
// ### "Model not found"
// 
// ```bash
// # Pull the required model
// ollama pull qwen2.5:latest
// ```
// 
// ### "Permission denied"
// 
// ```bash
// # Make sure virtual environment is activated
// source venv/bin/activate
// 
// # Reinstall if needed
// pip install -e .
// ```
// 
// ### Import errors
// 
// ```bash
// # Check installation
// pip list | grep localresearcher
// 
// # Reinstall dependencies
// pip install -e .
// ```
// 
// ## Next Steps
// 
// - Read the [Architecture docs](ARCHITECTURE.md)
// - Check out [examples](../examples/)
// - Explore advanced CLI options: `localresearcher ask --help`
// - Try analyzing PDFs and multiple files
// - Customize prompts in agent files
// 
// ## Common Use Cases
// 
// ### Research Assistant
// 
// ```bash
// localresearcher ask "Compare the pros and cons of different vector databases" \
//   --files research_paper.pdf
// ```
// 
// ### Document Summarization
// 
// ```bash
// localresearcher ask "Create an executive summary" \
//   --files quarterly_report.pdf notes.md
// ```
// 
// ### Meeting Notes Analysis
// 
// ```bash
// localresearcher ask "Extract action items and decisions" \
//   --files meeting_notes.txt
// ```
// 
// ### Code Documentation
// 
// ```bash
// localresearcher ask "Explain this codebase architecture" \
//   --files README.md ARCHITECTURE.md
// ```
// 
// ## Performance Tips
// 
// 1. **First run is slower**: Vector embeddings are cached
// 2. **Use smaller models for speed**: `ollama pull qwen2.5:7b`
// 3. **Adjust chunk size**: Edit `.env` → `CHUNK_SIZE=500`
// 4. **Run Ollama on GPU**: Automatically detected if available
// 
// ## Getting Help
// 
// - Issues: [GitHub Issues](https://github.com/yourusername/localresearcher-ai/issues)
// - Discussions: [GitHub Discussions](https://github.com/yourusername/localresearcher-ai/discussions)
// - Docs: [docs/](.)