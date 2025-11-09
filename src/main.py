#!/usr/bin/env python3
"""
ECO-STORM Main Entry Point
Command-line interface for the Economic Storm Analysis Platform
"""

import click
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from analyzers.economic_analyzer import EconomicAnalyzer
from models.predictor import CrisisPredictor
from data.loader import DataLoader


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """ECO-STORM: Economic Storm Analysis Platform"""
    pass


@cli.command()
@click.option('--data', '-d', type=click.Path(exists=True), required=True,
              help='Path to economic data file (CSV format)')
@click.option('--output', '-o', type=click.Path(), default='analysis_report.txt',
              help='Output file for analysis report')
def analyze(data, output):
    """Run economic analysis on provided data"""
    click.echo(f"Loading data from {data}...")
    
    try:
        loader = DataLoader()
        df = loader.load_csv(data)
        
        click.echo(f"Loaded {len(df)} records")
        click.echo("Running economic analysis...")
        
        analyzer = EconomicAnalyzer()
        results = analyzer.analyze(df)
        
        # Display results
        click.echo("\n=== Analysis Results ===")
        click.echo(f"Risk Score: {results.get('risk_score', 'N/A')}")
        click.echo(f"Volatility Index: {results.get('volatility_index', 'N/A')}")
        click.echo(f"Crisis Probability: {results.get('crisis_probability', 'N/A')}")
        
        # Save report
        with open(output, 'w') as f:
            f.write("ECO-STORM Analysis Report\n")
            f.write("=" * 50 + "\n\n")
            for key, value in results.items():
                f.write(f"{key}: {value}\n")
        
        click.echo(f"\nFull report saved to {output}")
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--data', '-d', type=click.Path(exists=True), required=True,
              help='Path to economic data file')
@click.option('--horizon', '-h', type=int, default=12,
              help='Prediction horizon in months')
def predict(data, horizon):
    """Predict future economic conditions"""
    click.echo(f"Loading data from {data}...")
    
    try:
        loader = DataLoader()
        df = loader.load_csv(data)
        
        click.echo(f"Running predictions for {horizon} months ahead...")
        
        predictor = CrisisPredictor()
        predictions = predictor.predict(df, horizon=horizon)
        
        click.echo("\n=== Predictions ===")
        for i, pred in enumerate(predictions, 1):
            click.echo(f"Month {i}: Crisis Probability = {pred:.2%}")
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--port', '-p', type=int, default=5000,
              help='Port for dashboard server')
def dashboard(port):
    """Launch the web dashboard"""
    click.echo(f"Starting ECO-STORM dashboard on port {port}...")
    click.echo("Dashboard functionality coming soon!")
    click.echo(f"Navigate to http://localhost:{port} once available")


@cli.command()
def info():
    """Display platform information"""
    click.echo("ECO-STORM: Economic Storm Analysis Platform")
    click.echo("Version: 0.1.0")
    click.echo("Author: Dr-Ai")
    click.echo("\nFor more information, visit:")
    click.echo("https://github.com/ELMOURABEA/ECO-STORM")


def main():
    """Main entry point"""
    cli()


if __name__ == '__main__':
    main()
