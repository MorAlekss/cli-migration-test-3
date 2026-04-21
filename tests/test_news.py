import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from src.news import get_top_stories, get_story

@pytest.mark.asyncio
async def test_get_top_stories():
    mock_response = MagicMock()
    mock_response.json.return_value = list(range(20))
    mock_response.raise_for_status.return_value = None
    with patch('src.news.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await get_top_stories()
        assert len(result) == 10

@pytest.mark.asyncio
async def test_get_story():
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "title": "Test"}
    mock_response.raise_for_status.return_value = None
    with patch('src.news.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await get_story(1)
        assert result["id"] == 1
