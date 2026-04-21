from unittest.mock import patch, MagicMock
from src.weather import get_weather, get_temperature

def test_get_weather():
    mock_response = MagicMock()
    mock_response.json.return_value = {"current_condition": [{"temp_C": "20"}]}
    mock_response.raise_for_status.return_value = None
    with patch('src.weather.requests.get', return_value=mock_response):
        result = get_weather("London")
        assert "current_condition" in result

def test_get_temperature():
    mock_response = MagicMock()
    mock_response.json.return_value = {"current_condition": [{"temp_C": "20"}]}
    mock_response.raise_for_status.return_value = None
    with patch('src.weather.requests.get', return_value=mock_response):
        assert get_temperature("London") == "20"
