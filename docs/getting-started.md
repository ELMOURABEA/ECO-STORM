# Getting Started with ECO-STORM

This guide will help you get started with the Economic Storm Analysis Platform.

## Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed
- pip package manager
- Basic understanding of economic indicators
- (Optional) Node.js 14+ for dashboard features

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/ELMOURABEA/ECO-STORM.git
cd ECO-STORM
```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# For development (includes testing tools)
pip install -r requirements-dev.txt
```

### Step 4: Verify Installation

```bash
# Check if installation was successful
python src/main.py info
```

## Quick Start

### Using the Command Line Interface

ECO-STORM provides a command-line interface for quick analysis:

```bash
# Get help
python src/main.py --help

# Analyze economic data
python src/main.py analyze -d data/sample_data.csv -o report.txt

# Run predictions
python src/main.py predict -d data/sample_data.csv -h 12
```

### Using Python API

```python
from eco_storm import EconomicAnalyzer, DataLoader

# Load data
loader = DataLoader()
data = loader.get_sample_data()  # Or load from file

# Create analyzer
analyzer = EconomicAnalyzer()

# Run analysis
results = analyzer.analyze(data)

# View results
print(f"Risk Score: {results['risk_score']}")
print(f"Crisis Probability: {results['crisis_probability']}")
```

## Basic Concepts

### Economic Indicators

ECO-STORM analyzes various economic indicators:

- **GDP Growth**: Economic output growth rate
- **Unemployment Rate**: Percentage of unemployed workforce
- **Inflation Rate**: Rate of price increase (CPI)
- **Interest Rates**: Central bank policy rates
- **Market Indices**: Stock market performance
- **Trade Balance**: Exports minus imports

### Risk Score

The risk score is a composite metric (0-100) that indicates overall economic risk:
- **0-30**: Low risk, stable economy
- **30-60**: Moderate risk, watch for trends
- **60-100**: High risk, potential crisis

### Crisis Probability

A percentage estimate of the likelihood of an economic crisis in the near term.

## Working with Data

### Data Format

ECO-STORM accepts data in CSV, Excel, or JSON formats with these common columns:

```csv
date,gdp_growth,unemployment,inflation,interest_rate,market_index
2020-01-01,2.5,5.0,2.1,1.5,3000
2020-02-01,2.3,5.2,2.0,1.5,2950
...
```

### Sample Data

Generate sample data for testing:

```python
from eco_storm import DataLoader

loader = DataLoader()
sample_data = loader.get_sample_data()
loader.export_data(sample_data, 'my_sample_data.csv')
```

## Next Steps

- Read the [API Reference](api-reference.md) for detailed documentation
- Explore [Model Documentation](models.md) to understand the algorithms
- Check [Configuration Guide](configuration.md) for customization options
- Try the examples in the `/examples` directory

## Getting Help

- Open an issue on GitHub for bugs or questions
- Check existing issues and documentation
- Review the examples directory

## Common Issues

### Import Errors

If you encounter import errors, make sure you've activated the virtual environment and installed all dependencies.

### Data Loading Issues

Ensure your data file:
- Is in the correct format
- Has proper column names
- Contains numeric values for analysis columns

### Performance Issues

For large datasets:
- Use data sampling
- Enable caching
- Consider using parallel processing options

## License

ECO-STORM is licensed under GNU General Public License v2.0. See the LICENSE file for details.
