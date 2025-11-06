#!/usr/bin/env python3
"""
Basic Economic Analysis Example

This example demonstrates how to perform basic economic analysis
using the ECO-STORM platform.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from analyzers.economic_analyzer import EconomicAnalyzer
from data.loader import DataLoader


def main():
    print("ECO-STORM: Basic Analysis Example")
    print("=" * 50)
    
    # Step 1: Load sample data
    print("\n1. Loading sample data...")
    loader = DataLoader()
    data = loader.get_sample_data()
    print(f"   Loaded {len(data)} records")
    print(f"   Columns: {', '.join(data.columns)}")
    
    # Step 2: Initialize analyzer
    print("\n2. Initializing Economic Analyzer...")
    analyzer = EconomicAnalyzer()
    
    # Step 3: Run analysis
    print("\n3. Running economic analysis...")
    results = analyzer.analyze(data)
    
    # Step 4: Display results
    print("\n4. Analysis Results:")
    print("-" * 50)
    print(f"   Risk Score:         {results['risk_score']:.2f}/100")
    print(f"   Volatility Index:   {results['volatility_index']:.4f}")
    print(f"   Crisis Probability: {results['crisis_probability']:.2%}")
    
    print("\n   Trend Analysis:")
    for indicator, trend in results['trend_analysis'].items():
        print(f"      {indicator}: {trend}")
    
    # Step 5: Display summary
    print("\n5. Summary:")
    print("-" * 50)
    summary = analyzer.get_summary()
    print(summary)
    
    # Step 6: Interpretation
    print("\n6. Interpretation:")
    print("-" * 50)
    risk_score = results['risk_score']
    if risk_score < 30:
        print("   ✓ Low risk - Economy appears stable")
    elif risk_score < 60:
        print("   ⚠ Moderate risk - Monitor economic indicators")
    else:
        print("   ⚠ High risk - Potential economic instability")
    
    print("\n" + "=" * 50)
    print("Analysis complete!")


if __name__ == '__main__':
    main()
