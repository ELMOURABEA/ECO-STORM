# Model Documentation

This document describes the analytical models and algorithms used in the ECO-STORM platform.

## Overview

ECO-STORM uses a combination of statistical methods, machine learning algorithms, and economic theory to analyze data and predict economic crises.

## Core Models

### 1. Risk Score Calculation

The risk score is a composite metric (0-100) that represents overall economic risk.

#### Methodology

The risk score combines multiple economic indicators with weighted importance:

```python
risk_score = Σ(wi × volatility_i)
```

Where:
- `wi` = weight for indicator i
- `volatility_i` = normalized volatility of indicator i

#### Default Weights

| Indicator | Weight |
|-----------|--------|
| GDP Growth | 0.25 |
| Unemployment | 0.20 |
| Inflation | 0.18 |
| Interest Rate | 0.15 |
| Market Volatility | 0.12 |
| Trade Balance | 0.10 |

#### Interpretation

- **0-30**: Low risk, stable economic conditions
- **30-60**: Moderate risk, monitoring recommended
- **60-100**: High risk, potential crisis conditions

### 2. Volatility Analysis

Volatility measures the degree of variation in economic indicators over time.

#### Calculation

```python
volatility = σ / μ
```

Where:
- `σ` = standard deviation
- `μ` = mean (with small epsilon to avoid division by zero)

#### Applications

- Market stability assessment
- Risk quantification
- Trend identification
- Anomaly detection

### 3. Crisis Prediction Model

The crisis predictor estimates the probability of economic downturns.

#### Approach

Currently uses a simple baseline model for demonstration:

1. **Data Preparation**: Historical economic indicators
2. **Feature Engineering**: Calculate trends, volatilities, correlations
3. **Model Training**: Fit model to historical crisis data
4. **Prediction**: Generate probabilities for future periods

#### Advanced Models (Planned)

Future versions will implement:

- **Random Forest**: Ensemble learning for robust predictions
- **Gradient Boosting**: Sequential learning with error correction
- **LSTM Networks**: Deep learning for time series patterns
- **ARIMA**: Statistical time series forecasting

### 4. Trend Analysis

Identifies directional trends in economic indicators.

#### Classification

Trends are classified as:

- **Rising**: Slope > +0.01
- **Falling**: Slope < -0.01
- **Stable**: -0.01 ≤ Slope ≤ +0.01

#### Calculation

```python
slope = (value_end - value_start) / n_periods
```

### 5. Correlation Analysis

Examines relationships between different economic indicators.

#### Method

Uses Pearson correlation coefficient:

```python
r = Σ((xi - x̄)(yi - ȳ)) / √(Σ(xi - x̄)² × Σ(yi - ȳ)²)
```

#### Interpretation

- **r > 0.7**: Strong positive correlation
- **0.3 < r < 0.7**: Moderate positive correlation
- **-0.3 < r < 0.3**: Weak or no correlation
- **r < -0.3**: Negative correlation

## Economic Indicators

### Primary Indicators

#### GDP Growth Rate
- **Description**: Rate of change in Gross Domestic Product
- **Frequency**: Quarterly
- **Healthy Range**: 2-3% annually
- **Crisis Signal**: Negative growth or sharp decline

#### Unemployment Rate
- **Description**: Percentage of workforce without jobs
- **Frequency**: Monthly
- **Healthy Range**: 3-5%
- **Crisis Signal**: Rapid increase or sustained high levels

#### Inflation Rate (CPI)
- **Description**: Consumer Price Index change
- **Frequency**: Monthly
- **Healthy Range**: 1.5-2.5%
- **Crisis Signal**: Deflation or hyperinflation

#### Interest Rates
- **Description**: Central bank policy rates
- **Frequency**: Variable (policy meetings)
- **Healthy Range**: 0.5-3%
- **Crisis Signal**: Zero or negative rates, rapid changes

### Secondary Indicators

- **Stock Market Indices**: Overall market performance
- **Currency Exchange Rates**: Currency strength
- **Trade Balance**: Exports vs. imports
- **Consumer Confidence**: Public sentiment
- **Housing Market**: Real estate health
- **Manufacturing Index**: Industrial production

## Feature Importance

Different indicators have varying predictive power:

1. **GDP Growth** (25%): Primary economic health metric
2. **Unemployment** (20%): Labor market conditions
3. **Inflation** (18%): Price stability
4. **Interest Rates** (15%): Monetary policy stance
5. **Market Volatility** (12%): Investor sentiment
6. **Trade Balance** (10%): International competitiveness

## Model Limitations

### Current Limitations

1. **Simplified Models**: Current implementation uses basic statistical methods
2. **Limited Historical Data**: Requires substantial data for accurate predictions
3. **External Factors**: Cannot predict unexpected shocks (pandemics, wars)
4. **Regional Specificity**: Models may need calibration for different economies

### Future Improvements

1. **Deep Learning Integration**: LSTM and transformer networks
2. **Sentiment Analysis**: News and social media monitoring
3. **Network Effects**: Financial system interconnectedness
4. **Real-time Processing**: Live data streaming and analysis
5. **Multi-regional Models**: Country-specific and global models

## Validation and Testing

### Backtesting

Models should be validated against historical data:

```python
# Split data into training and testing sets
train_data = data[:split_point]
test_data = data[split_point:]

# Train model
predictor.train(train_data)

# Evaluate on test data
metrics = predictor.evaluate(test_data, true_labels)
```

### Performance Metrics

- **Accuracy**: Overall correct predictions
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1 Score**: Harmonic mean of precision and recall
- **AUC-ROC**: Area under receiver operating characteristic curve

## References

### Economic Theory

- Keynesian Economics
- Modern Monetary Theory
- Austrian Business Cycle Theory
- New Keynesian DSGE Models

### Technical References

- Box, G. E., & Jenkins, G. M. (1970). Time Series Analysis
- Goodfellow, I., et al. (2016). Deep Learning
- Hastie, T., et al. (2009). The Elements of Statistical Learning

## Configuration

Models can be configured via YAML:

```yaml
prediction:
  model:
    type: "ensemble"
    algorithms:
      - "random_forest"
      - "gradient_boosting"
```

See [Configuration Guide](configuration.md) for details.

## Contributing

To contribute new models or improve existing ones:

1. Implement model in `src/models/`
2. Add comprehensive tests
3. Document methodology
4. Benchmark against existing models
5. Submit pull request

See [Contributing Guidelines](../CONTRIBUTING.md) for details.
