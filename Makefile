# Makefile for ECO-STORM

.PHONY: help install install-dev test lint clean run examples docs

help:
	@echo "ECO-STORM - Economic Storm Analysis Platform"
	@echo ""
	@echo "Available commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make test         - Run test suite"
	@echo "  make lint         - Run code linters"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make run          - Run the CLI application"
	@echo "  make examples     - Run example scripts"
	@echo "  make docs         - Build documentation"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v

test-cov:
	pytest --cov=src tests/ --cov-report=html --cov-report=term

lint:
	@echo "Running flake8..."
	-flake8 src/ tests/ --max-line-length=100
	@echo "Running pylint..."
	-pylint src/
	@echo "Running black (check only)..."
	-black --check src/ tests/

format:
	black src/ tests/ examples/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .coverage htmlcov/ .pytest_cache/

run:
	python src/main.py info

examples:
	@echo "Running basic analysis example..."
	python examples/basic_analysis.py
	@echo ""
	@echo "Running crisis prediction example..."
	python examples/crisis_prediction.py

docs:
	@echo "Documentation available in docs/ directory"
	@echo "Open docs/README.md to get started"

setup:
	python setup.py develop

.DEFAULT_GOAL := help
