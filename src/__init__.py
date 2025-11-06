"""
ECO-STORM: Economic Storm Analysis Platform
Main package initialization
"""

__version__ = "0.1.0"
__author__ = "Dr-Ai"

from .analyzers.economic_analyzer import EconomicAnalyzer
from .models.predictor import CrisisPredictor
from .data.loader import DataLoader

__all__ = [
    "EconomicAnalyzer",
    "CrisisPredictor",
    "DataLoader",
]
