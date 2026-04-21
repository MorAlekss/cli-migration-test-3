import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from src.geo import geocode, reverse_geocode

@pytest.mark.asyncio
async def test_geocode():
    mock_response = MagicMock()
    mock_response.json.return_value = [{"lat": "51.5", "lon": "-0.1"}]
    mock_response.raise_for_status.return_value = None
    with patch('src.geo.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await geocode("London")
        assert len(result) == 1

@pytest.mark.asyncio
async def test_reverse_geocode():
    mock_response = MagicMock()
    mock_response.json.return_value = {"display_name": "London"}
    mock_response.raise_for_status.return_value = None
    with patch('src.geo.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await reverse_geocode(51.5, -0.1)
        assert "display_name" in result
