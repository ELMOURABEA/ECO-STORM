"""
Data Loader Module
Handles loading and preprocessing of economic data
"""

import pandas as pd
import numpy as np
from typing import Optional, Dict, Any, List
from pathlib import Path


class DataLoader:
    """
    Utility class for loading and preprocessing economic data
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Data Loader
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        
    def load_csv(self, filepath: str, **kwargs) -> pd.DataFrame:
        """
        Load data from CSV file
        
        Args:
            filepath: Path to CSV file
            **kwargs: Additional arguments for pd.read_csv
            
        Returns:
            Loaded DataFrame
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
            
        df = pd.read_csv(filepath, **kwargs)
        return self._preprocess(df)
    
    def load_excel(self, filepath: str, **kwargs) -> pd.DataFrame:
        """
        Load data from Excel file
        
        Args:
            filepath: Path to Excel file
            **kwargs: Additional arguments for pd.read_excel
            
        Returns:
            Loaded DataFrame
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
            
        df = pd.read_excel(filepath, **kwargs)
        return self._preprocess(df)
    
    def load_json(self, filepath: str, **kwargs) -> pd.DataFrame:
        """
        Load data from JSON file
        
        Args:
            filepath: Path to JSON file
            **kwargs: Additional arguments for pd.read_json
            
        Returns:
            Loaded DataFrame
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
            
        df = pd.read_json(filepath, **kwargs)
        return self._preprocess(df)
    
    def _preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess loaded data
        
        Args:
            df: Raw DataFrame
            
        Returns:
            Preprocessed DataFrame
        """
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        if self.config.get('fill_na', False):
            df = df.ffill().bfill()
        
        # Convert date columns if present
        date_columns = self.config.get('date_columns', [])
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        return df
    
    def validate_data(self, df: pd.DataFrame, 
                     required_columns: Optional[List[str]] = None) -> bool:
        """
        Validate data structure and content
        
        Args:
            df: DataFrame to validate
            required_columns: List of required column names
            
        Returns:
            True if validation passes
        """
        if df is None or len(df) == 0:
            return False
            
        if required_columns:
            missing_cols = set(required_columns) - set(df.columns)
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
        
        return True
    
    def get_sample_data(self) -> pd.DataFrame:
        """
        Generate sample economic data for testing
        
        Returns:
            Sample DataFrame
        """
        np.random.seed(42)
        n_samples = 100
        
        dates = pd.date_range(start='2015-01-01', periods=n_samples, freq='M')
        
        data = {
            'date': dates,
            'gdp_growth': np.random.normal(2.5, 1.0, n_samples),
            'unemployment': np.random.normal(5.0, 1.5, n_samples),
            'inflation': np.random.normal(2.0, 0.8, n_samples),
            'interest_rate': np.random.normal(1.5, 0.5, n_samples),
            'market_index': np.cumsum(np.random.normal(0, 2, n_samples)) + 100,
        }
        
        df = pd.DataFrame(data)
        return df
    
    def export_data(self, df: pd.DataFrame, filepath: str, 
                   format: str = 'csv') -> None:
        """
        Export DataFrame to file
        
        Args:
            df: DataFrame to export
            filepath: Output file path
            format: Output format ('csv', 'excel', 'json')
        """
        if format == 'csv':
            df.to_csv(filepath, index=False)
        elif format == 'excel':
            df.to_excel(filepath, index=False)
        elif format == 'json':
            df.to_json(filepath, orient='records', indent=2)
        else:
            raise ValueError(f"Unsupported format: {format}")
