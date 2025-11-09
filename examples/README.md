# ECO-STORM Examples

This directory contains example scripts demonstrating how to use the ECO-STORM platform.

## Available Examples

### 1. Basic Analysis (`basic_analysis.py`)

Demonstrates basic economic data analysis:
- Loading sample data
- Running analysis
- Interpreting results

**Run:**
```bash
python examples/basic_analysis.py
```

### 2. Crisis Prediction (`crisis_prediction.py`)

Shows how to predict economic crises:
- Loading historical data
- Making predictions
- Understanding feature importance
- Risk assessment

**Run:**
```bash
python examples/crisis_prediction.py
```

## Using Your Own Data

To use these examples with your own data:

1. Prepare your data in CSV format with columns like:
   - `date`: Date of observation
   - `gdp_growth`: GDP growth rate
   - `unemployment`: Unemployment rate
   - `inflation`: Inflation rate
   - `interest_rate`: Interest rate
   - `market_index`: Stock market index

2. Modify the examples to load your data:
   ```python
   data = loader.load_csv('path/to/your/data.csv')
   ```

3. Run the analysis

## Sample Data Format

```csv
date,gdp_growth,unemployment,inflation,interest_rate,market_index
2020-01-01,2.5,5.0,2.1,1.5,3000
2020-02-01,2.3,5.2,2.0,1.5,2950
2020-03-01,1.8,6.0,1.9,1.0,2500
...
```

## Next Steps

After running these examples:
- Read the [API Reference](../docs/api-reference.md)
- Explore [Model Documentation](../docs/models.md)
- Try modifying the examples for your use case
- Build your own analysis scripts

## Troubleshooting

### ImportError

If you get import errors, make sure you're running from the repository root or have installed the package:

```bash
pip install -e .
```

### Data Loading Issues

Ensure your data file:
- Exists at the specified path
- Is in proper CSV format
- Has the expected columns
- Contains numeric values

## Contributing Examples

Have a useful example? Contribute it:

1. Create a new example script
2. Add documentation here
3. Include comments in your code
4. Submit a pull request

See [Contributing Guidelines](../CONTRIBUTING.md) for details.
