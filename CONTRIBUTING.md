# Contributing to ECO-STORM

Thank you for your interest in contributing to the Economic Storm Analysis Platform! This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and collaborative environment.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
- Use a clear, descriptive title
- Provide detailed explanation of the proposed feature
- Explain why this enhancement would be useful
- Include examples if applicable

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Add tests** if applicable
4. **Update documentation** as needed
5. **Ensure tests pass** by running `pytest tests/`
6. **Submit a pull request** with a clear description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ECO-STORM.git
cd ECO-STORM

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks (if available)
pre-commit install
```

## Coding Standards

### Python Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Maximum line length: 100 characters
- Use type hints where appropriate
- Write docstrings for all public functions/classes

### Code Organization

- Keep functions focused and single-purpose
- Avoid deep nesting (max 3-4 levels)
- Use meaningful comments for complex logic
- Group related functionality into modules

### Testing

- Write unit tests for new functionality
- Maintain test coverage above 80%
- Use descriptive test names
- Test edge cases and error conditions

```python
def test_analyzer_calculates_risk_score():
    """Test that risk score calculation returns valid range"""
    analyzer = EconomicAnalyzer()
    data = get_sample_data()
    results = analyzer.analyze(data)
    assert 0 <= results['risk_score'] <= 100
```

## Commit Messages

Write clear, concise commit messages:

```
Add feature for crisis probability calculation

- Implement logistic regression model
- Add unit tests for new feature
- Update documentation
```

## Documentation

- Update README.md if adding new features
- Add docstrings to new functions/classes
- Update relevant documentation in `/docs`
- Include examples for new functionality

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_analyzer.py
```

## Code Review Process

All submissions require review. We aim to:
- Review PRs within 48 hours
- Provide constructive feedback
- Help improve code quality
- Maintain project standards

## Questions?

Feel free to open an issue for any questions about contributing!

## License

By contributing, you agree that your contributions will be licensed under the GNU General Public License v2.0.
