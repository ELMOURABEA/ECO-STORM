#!/bin/bash
# ECO-STORM Quick Start Script

set -e

echo "================================================"
echo "ECO-STORM: Economic Storm Analysis Platform"
echo "Quick Start Setup"
echo "================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Check if Python 3.8+
required_version="3.8"
if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then 
    echo "Error: Python 3.8 or higher is required"
    exit 1
fi

echo "✓ Python version OK"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Run basic test
echo "Running basic tests..."
python -c "from src.data.loader import DataLoader; loader = DataLoader(); data = loader.get_sample_data(); print(f'✓ Loaded {len(data)} sample records')"
echo ""

# Display help
echo "================================================"
echo "Setup Complete!"
echo "================================================"
echo ""
echo "To get started:"
echo ""
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Run an example:"
echo "     python examples/basic_analysis.py"
echo ""
echo "  3. View available commands:"
echo "     python src/main.py --help"
echo ""
echo "  4. Read the documentation:"
echo "     docs/getting-started.md"
echo ""
echo "Happy analyzing!"
echo "================================================"
