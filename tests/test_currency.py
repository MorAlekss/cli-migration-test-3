from unittest.mock import patch, MagicMock
from src.currency import get_rates, convert

def test_get_rates():
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"EUR": 0.92, "GBP": 0.79}}
    mock_response.raise_for_status.return_value = None
    with patch('src.currency.requests.get', return_value=mock_response):
        result = get_rates("USD")
        assert "EUR" in result

def test_convert():
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"EUR": 0.92}}
    mock_response.raise_for_status.return_value = None
    with patch('src.currency.requests.get', return_value=mock_response):
        result = convert(100, "USD", "EUR")
        assert result == 92.0
