from unittest.mock import patch, MagicMock
from src.news import get_top_stories, get_story

def test_get_top_stories():
    mock_response = MagicMock()
    mock_response.json.return_value = list(range(20))
    mock_response.raise_for_status.return_value = None
    with patch('src.news.requests.get', return_value=mock_response):
        result = get_top_stories()
        assert len(result) == 10

def test_get_story():
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "title": "Test"}
    mock_response.raise_for_status.return_value = None
    with patch('src.news.requests.get', return_value=mock_response):
        result = get_story(1)
        assert result["id"] == 1
