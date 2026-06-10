.PHONY: install test lint format clean run docker-build docker-up docker-down help

help:
	@echo "LocalResearcherAI - Development Commands"
	@echo ""
	@echo "install       Install package and dependencies"
	@echo "install-dev   Install with dev dependencies"
	@echo "test          Run tests"
	@echo "test-cov      Run tests with coverage"
	@echo "lint          Run linters (ruff, mypy)"
	@echo "format        Format code (black, ruff)"
	@echo "clean         Clean cache and build files"
	@echo "run           Run example query"
	@echo "docker-build  Build Docker image"
	@echo "docker-up     Start Docker services"
	@echo "docker-down   Stop Docker services"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

test-cov:
	pytest --cov=localresearcher --cov-report=html --cov-report=term

lint:
	ruff check src/
	mypy src/

format:
	black src/ tests/
	ruff check --fix src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf build/ dist/ htmlcov/ .coverage

run:
	localresearcher ask "What are the key trends in AI research?" --files examples/sample.md

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down