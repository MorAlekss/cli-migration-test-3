from unittest.mock import patch, MagicMock, AsyncMock
import pytest
from src.currency import get_rates, convert

@pytest.mark.asyncio
async def test_get_rates():
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"EUR": 0.92, "GBP": 0.79}}
    mock_response.raise_for_status.return_value = None
    with patch('src.currency.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await get_rates("USD")
        assert "EUR" in result

@pytest.mark.asyncio
async def test_convert():
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"EUR": 0.92}}
    mock_response.raise_for_status.return_value = None
    with patch('src.currency.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await convert(100, "USD", "EUR")
        assert result == 92.0
