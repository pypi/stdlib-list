# Contributing to stdlib-list

Thank you for your interest in contributing to `stdlib-list`! We welcome contributions from everyone.

## Overview

`stdlib-list` provides lists of Python standard library modules for Python versions 2.6 through 3.13. The project maintains high standards for code quality, documentation, and testing.

## Development Setup

We use a `Makefile` to streamline the development workflow. To get started:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pypi/stdlib-list.git
   cd stdlib-list
   ```

2. **Set up the development environment:**
   ```bash
   make dev
   ```
   This creates a Python virtual environment and installs all development dependencies.

## Code Quality Standards

We maintain high code quality standards using automated tools:

### Linting and Formatting

- **Ruff**: Used for code linting and formatting
- **MyPy**: Used for static type checking

Run linting checks:
```bash
make lint
```

Auto-format code:
```bash
make reformat
```

### Testing

We require **100% test coverage** for all code changes.

Run tests:
```bash
make test
```

If you're working on a specific test, you can run individual tests:
```bash
make test TESTS="test_name_pattern"
```

## Documentation

Documentation is built using Sphinx and hosted at [pypi.github.io/stdlib-list](https://pypi.github.io/stdlib-list/).

Build documentation locally:
```bash
make doc
```

### Module Inclusion Policy

Please read our [module inclusion policy](docs/module-policy.rst) to understand how we determine which modules should be included in the standard library lists.

## Making Contributions

### Types of Contributions

We welcome several types of contributions:

1. **Bug reports**: If you find a missing or incorrectly included module
2. **Bug fixes**: Corrections to module lists or code issues
3. **Documentation improvements**: Clarifications or additions to docs
4. **New Python version support**: Adding support for new Python releases

### Submission Process

1. **Fork the repository** on GitHub
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following our code quality standards
4. **Run the full test suite** to ensure nothing is broken:
   ```bash
   make lint && make test
   ```
5. **Commit your changes** with a clear, descriptive commit message
6. **Push to your fork** and **create a pull request**

### Pull Request Guidelines

- Provide a clear description of the problem and solution
- Include tests for any new functionality
- Ensure all CI checks pass
- Keep changes focused and atomic
- Reference any related issues

### Code Style

- Follow Python PEP 8 (enforced by Ruff)
- Use type hints (checked by MyPy)
- Write clear, descriptive commit messages
- Add docstrings for new functions and classes

## Development Workflow Commands

Here's a quick reference of useful `make` commands:

| Command | Purpose |
|---------|---------|
| `make dev` | Set up development environment |
| `make lint` | Run linting and type checking |
| `make reformat` | Auto-format code with Ruff |
| `make test` | Run full test suite with coverage |
| `make doc` | Build documentation |
| `make package` | Build distribution packages |

## Getting Help

- **Issues**: For bug reports and feature requests, please use [GitHub Issues](https://github.com/pypi/stdlib-list/issues)
- **Discussions**: For questions about usage or contribution ideas
- **Documentation**: Check our [online documentation](https://pypi.github.io/stdlib-list/)

## Project History

This project was originally created by [@jackmaney](https://github.com/jackmaney) and later transferred to the PyPI organization with new maintainers. We appreciate all contributions that help maintain this valuable resource for the Python community.

Thank you for contributing! 🐍