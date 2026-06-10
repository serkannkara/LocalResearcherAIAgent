#!/bin/bash

set -e

echo "🔬 LocalResearcherAI - Installation Script"
echo "==========================================="
echo ""

# Check Python version
echo "📌 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.12+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
if (( $(echo "$PYTHON_VERSION < 3.12" | bc -l) )); then
    echo "❌ Python 3.12+ required. Current: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"
echo ""

# Check if Ollama is installed
echo "📌 Checking Ollama..."
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama is not installed."
    echo ""
    echo "Install Ollama:"
    echo "  macOS/Linux: curl -fsSL https://ollama.ai/install.sh | sh"
    echo "  Windows: Download from https://ollama.ai"
    echo ""
    read -p "Continue without Ollama? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✅ Ollama detected"
    
    # Check if models are pulled
    echo ""
    echo "📌 Checking Ollama models..."
    
    if ! ollama list | grep -q "qwen2.5"; then
        echo "⚠️  Model qwen2.5 not found"
        read -p "Pull qwen2.5:latest? (~4.7GB) (y/n) " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            ollama pull qwen2.5:latest
        fi
    else
        echo "✅ qwen2.5 model found"
    fi
    
    if ! ollama list | grep -q "nomic-embed-text"; then
        echo "⚠️  Model nomic-embed-text not found"
        read -p "Pull nomic-embed-text:latest? (~274MB) (y/n) " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            ollama pull nomic-embed-text:latest
        fi
    else
        echo "✅ nomic-embed-text model found"
    fi
fi

echo ""
echo "📦 Setting up virtual environment..."

# Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment exists"
fi

# Activate venv
source venv/bin/activate

echo ""
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -e .

echo ""
echo "📄 Setting up configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ Created .env file"
else
    echo "✅ .env file exists"
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "  1. Activate virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Test installation:"
echo "     localresearcher version"
echo ""
echo "  3. Run example:"
echo "     localresearcher ask \"What are AI trends?\" --files examples/sample.md"
echo ""
echo "For more info, see: docs/QUICKSTART.md"