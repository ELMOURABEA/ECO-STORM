"""
Unit tests for Data Loader
"""

import pytest
import pandas as pd
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from data.loader import DataLoader


class TestDataLoader:
    """Test cases for DataLoader class"""
    
    @pytest.fixture
    def loader(self):
        """Create loader instance"""
        return DataLoader()
    
    def test_loader_initialization(self, loader):
        """Test that loader initializes correctly"""
        assert loader is not None
        assert loader.config is not None
    
    def test_get_sample_data(self, loader):
        """Test sample data generation"""
        data = loader.get_sample_data()
        
        assert data is not None
        assert isinstance(data, pd.DataFrame)
        assert len(data) > 0
        assert 'gdp_growth' in data.columns
        assert 'unemployment' in data.columns
        assert 'inflation' in data.columns
    
    def test_load_csv(self, loader, tmp_path):
        """Test CSV loading"""
        # Create sample CSV
        sample_data = loader.get_sample_data()
        temp_file = tmp_path / "test.csv"
        sample_data.to_csv(temp_file, index=False)
        
        # Load it
        loaded = loader.load_csv(str(temp_file))
        
        assert loaded is not None
        assert len(loaded) > 0
    
    def test_load_nonexistent_file_raises_error(self, loader):
        """Test that loading nonexistent file raises error"""
        with pytest.raises(FileNotFoundError):
            loader.load_csv("nonexistent_file.csv")
    
    def test_validate_data(self, loader):
        """Test data validation"""
        data = loader.get_sample_data()
        
        # Valid data should pass
        assert loader.validate_data(data) is True
        
        # Empty data should fail
        empty_df = pd.DataFrame()
        assert loader.validate_data(empty_df) is False
    
    def test_validate_required_columns(self, loader):
        """Test validation with required columns"""
        data = loader.get_sample_data()
        
        # Should pass with existing columns
        required = ['gdp_growth', 'unemployment']
        assert loader.validate_data(data, required_columns=required) is True
        
        # Should raise error with missing columns
        with pytest.raises(ValueError):
            loader.validate_data(data, required_columns=['nonexistent_column'])
    
    def test_export_data_csv(self, loader, tmp_path):
        """Test exporting data to CSV"""
        data = loader.get_sample_data()
        output_file = tmp_path / "export.csv"
        
        loader.export_data(data, str(output_file), format='csv')
        
        assert output_file.exists()
        
        # Verify can be loaded back
        loaded = pd.read_csv(output_file)
        assert len(loaded) == len(data)
    
    def test_export_data_json(self, loader, tmp_path):
        """Test exporting data to JSON"""
        data = loader.get_sample_data()
        output_file = tmp_path / "export.json"
        
        loader.export_data(data, str(output_file), format='json')
        
        assert output_file.exists()


if __name__ == '__main__':
    pytest.main([__file__])
