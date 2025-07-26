#!/bin/bash

# Kotogram Setup Script
# This script sets up the development environment for the Kotogram project

set -e  # Exit on any error

echo "🚀 Setting up Kotogram development environment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}$1${NC}"
}

print_success() {
    echo -e "${GREEN}$1${NC}"
}

print_warning() {
    echo -e "${YELLOW}$1${NC}"
}

print_error() {
    echo -e "${RED}$1${NC}"
}

# Check if Python is available
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_success "Python3 is available: $PYTHON_VERSION"
        return 0
    elif command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version)
        print_success "Python is available: $PYTHON_VERSION"
        return 0
    else
        print_error "Python is not installed or not in PATH!"
        exit 1
    fi
}

# Get the appropriate Python command
get_python_cmd() {
    if command -v python3 &> /dev/null; then
        echo "python3"
    else
        echo "python"
    fi
}

# Check if virtualenv is available
check_virtualenv() {
    PYTHON_CMD=$(get_python_cmd)
    if $PYTHON_CMD -m virtualenv --version &> /dev/null; then
        VENV_VERSION=$($PYTHON_CMD -m virtualenv --version)
        print_success "virtualenv is available: $VENV_VERSION"
        return 0
    else
        print_warning "virtualenv is not installed. Installing now..."
        return 1
    fi
}

# Install virtualenv
install_virtualenv() {
    print_status "Installing virtualenv..."
    PYTHON_CMD=$(get_python_cmd)
    $PYTHON_CMD -m pip install virtualenv
    print_success "virtualenv installed successfully!"
}

# Create virtual environment
create_venv() {
    print_status "Creating virtual environment..."
    PYTHON_CMD=$(get_python_cmd)

    if [ -d ".venv" ]; then
        print_warning "Virtual environment already exists at .venv"
        return 0
    fi

    $PYTHON_CMD -m virtualenv .venv
    print_success "Virtual environment created successfully!"
}

# Activate virtual environment
activate_venv() {
    print_status "Activating virtual environment..."

    if [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate
        print_success "Virtual environment activated!"
    else
        print_error "Virtual environment activation script not found!"
        exit 1
    fi
}

# Install project dependencies
install_dependencies() {
    print_status "Installing project dependencies..."

    # Upgrade pip first
    pip install --upgrade pip

    # Install the project in editable mode
    pip install -e .

    # Install development dependencies
    pip install -e ".[dev]"

    print_success "Dependencies installed successfully!"
}

# Install and configure pre-commit
setup_pre_commit() {
    print_status "Setting up pre-commit hooks..."

    # Install pre-commit hooks
    pre-commit install

    # Run pre-commit on all files to ensure everything is properly formatted
    print_status "Running pre-commit on all files..."
    pre-commit run --all-files || {
        print_warning "Pre-commit found some issues. You may want to fix them manually."
        print_warning "Run 'pre-commit run --all-files' to see the issues."
    }

    print_success "Pre-commit hooks installed and configured!"
}

# Verify installation
verify_setup() {
    print_status "Verifying setup..."

    # Check if virtual environment exists
    if [ -d ".venv" ]; then
        print_success "Virtual environment created successfully!"
    else
        print_error "Virtual environment not found!"
        exit 1
    fi

    # Check if dependencies are installed
    if python -c "import janome, pydantic, pytest" 2>/dev/null; then
        print_success "Core dependencies verified!"
    else
        print_error "Some dependencies are missing!"
        exit 1
    fi

    # Check if pre-commit is working
    if pre-commit --version &> /dev/null; then
        print_success "Pre-commit is working correctly!"
    else
        print_error "Pre-commit is not working!"
        exit 1
    fi
}

# Main execution
main() {
    print_status "Starting Kotogram development environment setup..."

    # Check Python availability
    check_python

    # Check and install virtualenv if needed
    if ! check_virtualenv; then
        install_virtualenv
    fi

    # Create virtual environment
    create_venv

    # Activate virtual environment
    activate_venv

    # Install dependencies
    install_dependencies

    # Setup pre-commit
    setup_pre_commit

    # Verify everything is working
    verify_setup

    print_success "🎉 Kotogram development environment setup complete!"
    echo ""
    print_status "Next steps:"
    echo "  1. Activate the virtual environment: source .venv/bin/activate"
    echo "  2. Run tests: pytest"
    echo "  3. Start developing!"
    echo ""
    print_status "Useful commands:"
    echo "  - pytest                    # Run tests"
    echo "  - black .                   # Format code"
    echo "  - isort .                   # Sort imports"
    echo "  - flake8 .                  # Lint code"
    echo "  - mypy .                    # Type checking"
    echo "  - bandit -r .               # Security audit"
    echo "  - pre-commit run --all-files # Run all pre-commit hooks"
}

# Run main function
main "$@"
