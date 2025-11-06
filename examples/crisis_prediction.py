#!/usr/bin/env python3
"""
Crisis Prediction Example

This example demonstrates how to predict economic crises
using the ECO-STORM platform.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from models.predictor import CrisisPredictor
from data.loader import DataLoader


def main():
    print("ECO-STORM: Crisis Prediction Example")
    print("=" * 50)
    
    # Step 1: Load sample data
    print("\n1. Loading historical economic data...")
    loader = DataLoader()
    data = loader.get_sample_data()
    print(f"   Loaded {len(data)} historical records")
    
    # Step 2: Initialize predictor
    print("\n2. Initializing Crisis Predictor...")
    predictor = CrisisPredictor(model_type='simple')
    
    # Step 3: Make predictions
    print("\n3. Predicting crisis probabilities...")
    horizon = 12  # Predict 12 months ahead
    predictions = predictor.predict(data, horizon=horizon)
    
    # Step 4: Display predictions
    print(f"\n4. Predictions for next {horizon} months:")
    print("-" * 50)
    for i, prob in enumerate(predictions, 1):
        bar = '█' * int(prob * 50)
        print(f"   Month {i:2d}: {prob:.2%} {bar}")
    
    # Step 5: Feature importance
    print("\n5. Most Important Economic Indicators:")
    print("-" * 50)
    importance = predictor.get_feature_importance()
    sorted_features = sorted(importance.items(), key=lambda x: x[1], reverse=True)
    
    for feature, score in sorted_features:
        bar = '■' * int(score * 40)
        print(f"   {feature:20s}: {score:.2%} {bar}")
    
    # Step 6: Risk assessment
    print("\n6. Risk Assessment:")
    print("-" * 50)
    avg_prob = sum(predictions) / len(predictions)
    
    if avg_prob < 0.2:
        risk_level = "LOW"
        message = "Economic conditions appear stable"
    elif avg_prob < 0.5:
        risk_level = "MODERATE"
        message = "Some economic uncertainty detected"
    else:
        risk_level = "HIGH"
        message = "Significant crisis risk identified"
    
    print(f"   Risk Level: {risk_level}")
    print(f"   Average Crisis Probability: {avg_prob:.2%}")
    print(f"   Assessment: {message}")
    
    print("\n" + "=" * 50)
    print("Prediction complete!")


if __name__ == '__main__':
    main()
