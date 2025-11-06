"""
Unit tests for Economic Analyzer
"""

import pytest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from analyzers.economic_analyzer import EconomicAnalyzer
from data.loader import DataLoader


class TestEconomicAnalyzer:
    """Test cases for EconomicAnalyzer class"""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing"""
        loader = DataLoader()
        return loader.get_sample_data()
    
    @pytest.fixture
    def analyzer(self):
        """Create analyzer instance"""
        return EconomicAnalyzer()
    
    def test_analyzer_initialization(self, analyzer):
        """Test that analyzer initializes correctly"""
        assert analyzer is not None
        assert analyzer.config is not None
        assert analyzer.data is None
    
    def test_load_data(self, analyzer, sample_data, tmp_path):
        """Test data loading functionality"""
        # Save sample data to temp file
        temp_file = tmp_path / "test_data.csv"
        sample_data.to_csv(temp_file, index=False)
        
        # Load data
        loaded_data = analyzer.load_data(str(temp_file))
        
        assert loaded_data is not None
        assert len(loaded_data) > 0
        assert analyzer.data is not None
    
    def test_analyze_returns_results(self, analyzer, sample_data):
        """Test that analyze method returns results"""
        results = analyzer.analyze(sample_data)
        
        assert results is not None
        assert isinstance(results, dict)
        assert 'risk_score' in results
        assert 'volatility_index' in results
        assert 'crisis_probability' in results
    
    def test_risk_score_in_valid_range(self, analyzer, sample_data):
        """Test that risk score is in valid range (0-100)"""
        results = analyzer.analyze(sample_data)
        risk_score = results['risk_score']
        
        assert 0 <= risk_score <= 100
    
    def test_crisis_probability_in_valid_range(self, analyzer, sample_data):
        """Test that crisis probability is between 0 and 1"""
        results = analyzer.analyze(sample_data)
        crisis_prob = results['crisis_probability']
        
        assert 0 <= crisis_prob <= 1
    
    def test_volatility_calculation(self, analyzer, sample_data):
        """Test volatility index calculation"""
        results = analyzer.analyze(sample_data)
        volatility = results['volatility_index']
        
        assert isinstance(volatility, float)
        assert volatility >= 0
    
    def test_trend_analysis(self, analyzer, sample_data):
        """Test trend analysis functionality"""
        results = analyzer.analyze(sample_data)
        trends = results['trend_analysis']
        
        assert isinstance(trends, dict)
        assert len(trends) > 0
        
        # Check valid trend values
        valid_trends = {'rising', 'falling', 'stable'}
        for trend in trends.values():
            assert trend in valid_trends
    
    def test_analyze_without_data_raises_error(self, analyzer):
        """Test that analyzing without data raises error"""
        with pytest.raises(ValueError):
            analyzer.analyze()
    
    def test_get_summary(self, analyzer, sample_data):
        """Test summary generation"""
        analyzer.analyze(sample_data)
        summary = analyzer.get_summary()
        
        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'Risk Score' in summary
    
    def test_empty_dataframe_handling(self, analyzer):
        """Test handling of empty DataFrame"""
        empty_df = pd.DataFrame()
        results = analyzer.analyze(empty_df)
        
        # Should return default values
        assert results['risk_score'] == 0.0


if __name__ == '__main__':
    pytest.main([__file__])
