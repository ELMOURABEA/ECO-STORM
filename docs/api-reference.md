# API Reference

Complete API documentation for the ECO-STORM platform.

## Table of Contents

- [Core Classes](#core-classes)
  - [EconomicAnalyzer](#economicanalyzer)
  - [CrisisPredictor](#crisispredictor)
  - [DataLoader](#dataloader)

---

## Core Classes

### EconomicAnalyzer

Main class for performing economic analysis.

#### Constructor

```python
EconomicAnalyzer(config: Optional[Dict[str, Any]] = None)
```

**Parameters:**
- `config` (dict, optional): Configuration dictionary for analyzer settings

**Example:**
```python
analyzer = EconomicAnalyzer(config={'risk_threshold': 0.7})
```

#### Methods

##### `load_data(filepath: str) -> pd.DataFrame`

Load economic data from a file.

**Parameters:**
- `filepath` (str): Path to the data file

**Returns:**
- `pd.DataFrame`: Loaded data

**Example:**
```python
data = analyzer.load_data('data/economic_data.csv')
```

##### `analyze(data: Optional[pd.DataFrame] = None) -> Dict[str, Any]`

Perform comprehensive economic analysis.

**Parameters:**
- `data` (pd.DataFrame, optional): Data to analyze. Uses previously loaded data if not provided.

**Returns:**
- `dict`: Analysis results containing:
  - `risk_score` (float): Overall risk score (0-100)
  - `volatility_index` (float): Market volatility measure
  - `crisis_probability` (float): Crisis probability (0-1)
  - `trend_analysis` (dict): Trend indicators for each metric
  - `correlation_matrix` (pd.DataFrame): Correlation matrix

**Example:**
```python
results = analyzer.analyze(data)
print(f"Risk Score: {results['risk_score']}")
```

##### `get_summary() -> str`

Get a formatted text summary of the analysis.

**Returns:**
- `str`: Formatted summary text

**Example:**
```python
summary = analyzer.get_summary()
print(summary)
```

---

### CrisisPredictor

Class for predicting economic crises.

#### Constructor

```python
CrisisPredictor(model_type: str = 'simple')
```

**Parameters:**
- `model_type` (str): Type of prediction model ('simple', 'advanced', 'ensemble')

**Example:**
```python
predictor = CrisisPredictor(model_type='ensemble')
```

#### Methods

##### `train(data: pd.DataFrame, labels: Optional[pd.Series] = None) -> None`

Train the prediction model.

**Parameters:**
- `data` (pd.DataFrame): Training data
- `labels` (pd.Series, optional): Target labels for supervised learning

**Example:**
```python
predictor.train(historical_data, crisis_labels)
```

##### `predict(data: pd.DataFrame, horizon: int = 12) -> List[float]`

Predict crisis probabilities for future periods.

**Parameters:**
- `data` (pd.DataFrame): Historical economic data
- `horizon` (int): Number of periods to predict (default: 12)

**Returns:**
- `List[float]`: List of crisis probabilities for each future period

**Example:**
```python
predictions = predictor.predict(data, horizon=6)
for i, prob in enumerate(predictions, 1):
    print(f"Month {i}: {prob:.2%}")
```

##### `predict_single(data: pd.DataFrame) -> float`

Predict crisis probability for the next period only.

**Parameters:**
- `data` (pd.DataFrame): Historical economic data

**Returns:**
- `float`: Crisis probability for next period

**Example:**
```python
next_month_prob = predictor.predict_single(data)
```

##### `get_feature_importance() -> Dict[str, float]`

Get importance scores for different economic indicators.

**Returns:**
- `dict`: Mapping of feature names to importance scores

**Example:**
```python
importance = predictor.get_feature_importance()
for feature, score in importance.items():
    print(f"{feature}: {score:.2%}")
```

---

### DataLoader

Utility class for loading and preprocessing economic data.

#### Constructor

```python
DataLoader(config: Optional[Dict[str, Any]] = None)
```

**Parameters:**
- `config` (dict, optional): Configuration for data loading

**Example:**
```python
loader = DataLoader(config={'fill_na': True})
```

#### Methods

##### `load_csv(filepath: str, **kwargs) -> pd.DataFrame`

Load data from CSV file.

**Parameters:**
- `filepath` (str): Path to CSV file
- `**kwargs`: Additional arguments passed to `pd.read_csv`

**Returns:**
- `pd.DataFrame`: Loaded and preprocessed data

**Example:**
```python
data = loader.load_csv('data.csv', parse_dates=['date'])
```

##### `load_excel(filepath: str, **kwargs) -> pd.DataFrame`

Load data from Excel file.

**Parameters:**
- `filepath` (str): Path to Excel file
- `**kwargs`: Additional arguments passed to `pd.read_excel`

**Returns:**
- `pd.DataFrame`: Loaded and preprocessed data

##### `load_json(filepath: str, **kwargs) -> pd.DataFrame`

Load data from JSON file.

**Parameters:**
- `filepath` (str): Path to JSON file
- `**kwargs`: Additional arguments passed to `pd.read_json`

**Returns:**
- `pd.DataFrame`: Loaded and preprocessed data

##### `get_sample_data() -> pd.DataFrame`

Generate sample economic data for testing.

**Returns:**
- `pd.DataFrame`: Sample data with typical economic indicators

**Example:**
```python
sample_data = loader.get_sample_data()
```

##### `validate_data(df: pd.DataFrame, required_columns: Optional[List[str]] = None) -> bool`

Validate data structure and content.

**Parameters:**
- `df` (pd.DataFrame): DataFrame to validate
- `required_columns` (list, optional): List of required column names

**Returns:**
- `bool`: True if validation passes

**Raises:**
- `ValueError`: If required columns are missing

**Example:**
```python
is_valid = loader.validate_data(data, required_columns=['gdp', 'inflation'])
```

##### `export_data(df: pd.DataFrame, filepath: str, format: str = 'csv') -> None`

Export DataFrame to file.

**Parameters:**
- `df` (pd.DataFrame): Data to export
- `filepath` (str): Output file path
- `format` (str): Output format ('csv', 'excel', 'json')

**Example:**
```python
loader.export_data(processed_data, 'output.csv', format='csv')
```

---

## Error Handling

All methods raise appropriate exceptions:

- `FileNotFoundError`: When specified file doesn't exist
- `ValueError`: For invalid parameters or data
- `TypeError`: For incorrect data types

**Example:**
```python
try:
    data = loader.load_csv('nonexistent.csv')
except FileNotFoundError as e:
    print(f"Error: {e}")
```

---

## Type Hints

The library uses Python type hints for better code clarity:

```python
from typing import Dict, List, Optional, Any
import pandas as pd
```

---

## Additional Resources

- [Getting Started Guide](getting-started.md)
- [Model Documentation](models.md)
- [Configuration Guide](configuration.md)
- [GitHub Repository](https://github.com/ELMOURABEA/ECO-STORM)
