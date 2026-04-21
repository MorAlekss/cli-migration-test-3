from unittest.mock import patch, MagicMock
from src.geo import geocode, reverse_geocode

def test_geocode():
    mock_response = MagicMock()
    mock_response.json.return_value = [{"lat": "51.5", "lon": "-0.1"}]
    mock_response.raise_for_status.return_value = None
    with patch('src.geo.requests.get', return_value=mock_response):
        result = geocode("London")
        assert len(result) == 1

def test_reverse_geocode():
    mock_response = MagicMock()
    mock_response.json.return_value = {"display_name": "London"}
    mock_response.raise_for_status.return_value = None
    with patch('src.geo.requests.get', return_value=mock_response):
        result = reverse_geocode(51.5, -0.1)
        assert "display_name" in result
