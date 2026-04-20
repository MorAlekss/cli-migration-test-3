import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from src.weather import get_weather, get_temperature

@pytest.mark.asyncio
async def test_get_weather():
    mock_response = MagicMock()
    mock_response.json.return_value = {"current_condition": [{"temp_C": "20"}]}
    mock_response.raise_for_status.return_value = None
    with patch('src.weather.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await get_weather("London")
        assert "current_condition" in result

@pytest.mark.asyncio
async def test_get_temperature():
    mock_response = MagicMock()
    mock_response.json.return_value = {"current_condition": [{"temp_C": "20"}]}
    mock_response.raise_for_status.return_value = None
    with patch('src.weather.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        assert await get_temperature("London") == "20"
