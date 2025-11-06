# Configuration Guide

This guide explains how to configure the ECO-STORM platform for your specific needs.

## Configuration Files

### Main Configuration

The primary configuration file is located at `config/default_config.yaml`.

## Configuration Sections

### Application Settings

```yaml
app:
  name: "ECO-STORM"
  version: "0.1.0"
  debug: false
```

- `name`: Application name
- `version`: Version number
- `debug`: Enable debug mode (true/false)

### Data Settings

```yaml
data:
  sources:
    - type: "csv"
      path: "data/economic_indicators.csv"
  
  preprocessing:
    fill_missing: true
    remove_outliers: true
    normalize: true
  
  date_columns:
    - "date"
    - "timestamp"
```

#### Data Sources

Configure multiple data sources:

- `type`: Data source type ('csv', 'excel', 'json', 'api')
- `path`: File path or API endpoint
- Additional type-specific parameters

#### Preprocessing Options

- `fill_missing`: Fill missing values (true/false)
- `remove_outliers`: Remove statistical outliers (true/false)
- `normalize`: Normalize numeric data (true/false)

### Analysis Settings

```yaml
analysis:
  risk_score:
    method: "weighted_average"
    weights:
      gdp_growth: 0.25
      unemployment: 0.20
      inflation: 0.18
      interest_rate: 0.15
      market_volatility: 0.12
      trade_balance: 0.10
```

#### Risk Score Weights

Customize the importance of different economic indicators:

```yaml
weights:
  indicator_name: weight_value
```

Total weights should sum to 1.0.

#### Volatility Settings

```yaml
volatility:
  window_size: 30
  method: "rolling_std"
```

- `window_size`: Rolling window size for calculations
- `method`: Calculation method ('rolling_std', 'exponential')

### Prediction Settings

```yaml
prediction:
  model:
    type: "ensemble"
    algorithms:
      - "random_forest"
      - "gradient_boosting"
      - "lstm"
  
  training:
    test_size: 0.2
    validation_size: 0.1
    random_state: 42
  
  horizon:
    default: 12
    min: 1
    max: 36
```

#### Model Configuration

- `type`: Model type ('simple', 'advanced', 'ensemble')
- `algorithms`: List of algorithms to use (for ensemble)

#### Training Parameters

- `test_size`: Proportion of data for testing (0-1)
- `validation_size`: Proportion for validation (0-1)
- `random_state`: Random seed for reproducibility

#### Prediction Horizon

- `default`: Default months to predict
- `min`/`max`: Allowed range

### Alert Settings

```yaml
alerts:
  enabled: true
  thresholds:
    risk_score: 70
    crisis_probability: 0.60
    volatility_index: 0.30
  
  notifications:
    email: false
    slack: false
    console: true
```

#### Threshold Configuration

Set alert thresholds for different metrics:

- `risk_score`: Trigger when score exceeds this value (0-100)
- `crisis_probability`: Trigger when probability exceeds this (0-1)
- `volatility_index`: Trigger when volatility exceeds this

#### Notification Channels

Enable/disable notification methods:

- `email`: Email notifications
- `slack`: Slack notifications
- `console`: Console output

### Dashboard Settings

```yaml
dashboard:
  host: "localhost"
  port: 5000
  refresh_interval: 300
  
  charts:
    default_theme: "light"
    colors:
      risk_low: "#28a745"
      risk_medium: "#ffc107"
      risk_high: "#dc3545"
```

- `host`: Dashboard host address
- `port`: Port number
- `refresh_interval`: Data refresh interval (seconds)
- `charts`: Visualization settings

### Logging Settings

```yaml
logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: "logs/eco_storm.log"
  console: true
```

#### Log Levels

- `DEBUG`: Detailed debugging information
- `INFO`: General information
- `WARNING`: Warning messages
- `ERROR`: Error messages
- `CRITICAL`: Critical errors

## Using Configuration in Code

### Loading Configuration

```python
import yaml

with open('config/default_config.yaml', 'r') as f:
    config = yaml.safe_load(f)
```

### Passing to Components

```python
from eco_storm import EconomicAnalyzer

# Pass config to analyzer
analyzer = EconomicAnalyzer(config=config['analysis'])
```

## Environment Variables

Override configuration with environment variables:

```bash
export ECO_STORM_DEBUG=true
export ECO_STORM_DATA_PATH=/path/to/data
export ECO_STORM_PORT=8000
```

### Loading Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

debug = os.getenv('ECO_STORM_DEBUG', 'false') == 'true'
data_path = os.getenv('ECO_STORM_DATA_PATH', 'data/')
```

## Custom Configuration Files

Create custom configuration files for different environments:

```bash
config/
├── default_config.yaml
├── development.yaml
├── production.yaml
└── testing.yaml
```

### Loading Custom Config

```python
import sys
import yaml

env = sys.argv[1] if len(sys.argv) > 1 else 'default'
config_file = f'config/{env}_config.yaml'

with open(config_file, 'r') as f:
    config = yaml.safe_load(f)
```

## Best Practices

### Security

- Never commit sensitive data (API keys, passwords) to configuration files
- Use environment variables for secrets
- Use `.env` files for local development (add to `.gitignore`)

### Organization

- Keep related settings together
- Use clear, descriptive names
- Document custom settings
- Maintain consistent formatting

### Validation

Validate configuration on startup:

```python
def validate_config(config):
    """Validate configuration structure"""
    required_keys = ['app', 'data', 'analysis']
    
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required config section: {key}")
    
    return True
```

## Troubleshooting

### Configuration Not Loading

1. Check file path is correct
2. Verify YAML syntax (use online YAML validator)
3. Ensure file has proper permissions

### Invalid Values

1. Check data types (string, number, boolean)
2. Verify value ranges
3. Ensure required fields are present

### Performance Issues

1. Adjust `window_size` for analysis
2. Reduce `refresh_interval` for dashboard
3. Optimize data preprocessing settings

## Additional Resources

- [Getting Started Guide](getting-started.md)
- [API Reference](api-reference.md)
- [YAML Syntax Guide](https://yaml.org/spec/1.2/spec.html)
