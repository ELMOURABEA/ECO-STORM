# ECO-STORM Documentation

Welcome to the ECO-STORM (Economic Storm Analysis Platform) documentation.

## Documentation Index

### Getting Started

- **[Getting Started Guide](getting-started.md)** - Installation, setup, and quick start
  - Prerequisites
  - Installation steps
  - Basic usage examples
  - Common issues and troubleshooting

### Reference Documentation

- **[API Reference](api-reference.md)** - Complete API documentation
  - EconomicAnalyzer class
  - CrisisPredictor class
  - DataLoader class
  - Method signatures and examples

- **[Model Documentation](models.md)** - Model methodology and theory
  - Risk score calculation
  - Volatility analysis
  - Crisis prediction models
  - Economic indicators
  - Model limitations

- **[Configuration Guide](configuration.md)** - Configuration options
  - Configuration file structure
  - Application settings
  - Data settings
  - Analysis parameters
  - Alert configuration
  - Environment variables

### User Guides

- **[Examples](../examples/README.md)** - Code examples
  - Basic analysis example
  - Crisis prediction example
  - Custom data usage

### Developer Documentation

- **[Contributing Guidelines](../CONTRIBUTING.md)** - How to contribute
  - Code of conduct
  - Development setup
  - Coding standards
  - Testing requirements
  - Pull request process

## Quick Links

### For New Users

1. Start with the [Getting Started Guide](getting-started.md)
2. Try the [Examples](../examples/README.md)
3. Read the [API Reference](api-reference.md)

### For Developers

1. Review [Contributing Guidelines](../CONTRIBUTING.md)
2. Understand the [Models](models.md)
3. Check [Configuration Guide](configuration.md)

### For Data Scientists

1. Read [Model Documentation](models.md)
2. Review economic indicators section
3. Explore prediction algorithms
4. Check feature importance

## Key Concepts

### Economic Storm

An "economic storm" refers to periods of significant economic instability, crisis, or downturn characterized by:
- Sharp market declines
- Rising unemployment
- Credit crunches
- Currency instability
- Loss of confidence

### Risk Assessment

The platform evaluates risk through:
- **Risk Score (0-100)**: Composite metric of economic health
- **Volatility Index**: Measure of market instability
- **Crisis Probability**: Likelihood of imminent crisis

### Predictive Analysis

Uses historical data to forecast:
- Future economic conditions
- Crisis probabilities
- Trend directions
- Leading indicators

## Platform Architecture

```
ECO-STORM
├── Data Layer (src/data/)
│   └── Load, validate, preprocess data
│
├── Analysis Layer (src/analyzers/)
│   └── Calculate metrics, detect patterns
│
├── Prediction Layer (src/models/)
│   └── Forecast future conditions
│
└── Interface Layer
    ├── CLI (src/main.py)
    └── Dashboard (dashboard/)
```

## Economic Indicators Monitored

| Indicator | Description | Importance |
|-----------|-------------|------------|
| GDP Growth | Economic output | High |
| Unemployment | Labor market | High |
| Inflation | Price stability | High |
| Interest Rates | Monetary policy | Medium |
| Market Indices | Investor sentiment | Medium |
| Trade Balance | External sector | Medium |

## Use Cases

### 1. Economic Monitoring
- Track real-time economic indicators
- Monitor trends and changes
- Set up alerts for significant events

### 2. Risk Assessment
- Evaluate current economic risk
- Compare to historical levels
- Identify warning signs

### 3. Crisis Prediction
- Forecast future economic conditions
- Estimate crisis probabilities
- Plan risk mitigation strategies

### 4. Research and Analysis
- Study historical economic patterns
- Test economic theories
- Validate prediction models

## Supported Data Formats

- **CSV**: Comma-separated values
- **Excel**: .xlsx and .xls files
- **JSON**: JavaScript Object Notation
- **API**: REST API endpoints (planned)

## System Requirements

### Minimum Requirements
- Python 3.8+
- 4GB RAM
- 1GB disk space

### Recommended
- Python 3.10+
- 8GB RAM
- 2GB disk space
- SSD storage

## Browser Support (Dashboard)

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

ECO-STORM is licensed under GNU General Public License v2.0.

See [LICENSE](../LICENSE) for full text.

## Support

### Getting Help

- Check documentation first
- Search existing [GitHub Issues](https://github.com/ELMOURABEA/ECO-STORM/issues)
- Open a new issue if needed

### Community

- GitHub Discussions (coming soon)
- Issue tracker for bugs
- Pull requests for contributions

## Changelog

### Version 0.1.0 (Initial Release)

- Core analysis framework
- Basic prediction models
- CLI interface
- Comprehensive documentation
- Example scripts
- Test suite

## Roadmap

### Upcoming Features

- [ ] Real-time data streaming
- [ ] Advanced ML models (LSTM, Transformers)
- [ ] Interactive web dashboard
- [ ] Multi-region support
- [ ] API endpoints
- [ ] Sentiment analysis integration
- [ ] Mobile app

### Future Enhancements

- [ ] Cloud deployment support
- [ ] Database integration
- [ ] User authentication
- [ ] Custom model training
- [ ] Export/import configurations
- [ ] Automated reporting

## Contributing to Documentation

Documentation improvements are welcome! To contribute:

1. Fork the repository
2. Edit markdown files in `docs/`
3. Submit a pull request
4. Follow markdown best practices

See [Contributing Guidelines](../CONTRIBUTING.md) for details.

## Additional Resources

### External Resources

- [World Bank Open Data](https://data.worldbank.org/)
- [IMF Data](https://www.imf.org/en/Data)
- [FRED Economic Data](https://fred.stlouisfed.org/)
- [OECD Statistics](https://stats.oecd.org/)

### Academic References

- Economic theory papers
- Machine learning research
- Time series analysis
- Financial modeling

---

**Last Updated**: November 2025
**Version**: 0.1.0
