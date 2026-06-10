"""Basic tests for LocalResearcherAI."""

import pytest
from localresearcher import __version__


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_imports():
    """Test that core modules can be imported."""
    from localresearcher.core import config, schemas
    from localresearcher.llm import ollama
    from localresearcher.agents import planner
    
    assert config is not None
    assert schemas is not None
    assert ollama is not None
    assert planner is not None