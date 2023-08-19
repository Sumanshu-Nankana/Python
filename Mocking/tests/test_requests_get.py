import pytest
from src.requests_code import get_posts
from unittest.mock import Mock
from tests.examples import get_posts_response

# This is also correct
# @pytest.fixture
# def context(monkeypatch):
#     mock_get = Mock(return_value=Mock(status_code=200, json=lambda: get_posts_response))
#     monkeypatch.setattr('src.code.requests.get', mock_get)
#     yield mock_get

# Another more simplified approach (Easy to understand)
@pytest.fixture
def context(monkeypatch):
     mock_response = Mock()
     mock_response.status_code = 200
     mock_response.json = lambda: get_posts_response
     mock_get = Mock(return_value=mock_response)
     monkeypatch.setattr('src.requests_code.requests.get', mock_get)
     yield mock_get
#
#
@pytest.fixture
def context_exception(monkeypatch):
    mock_get = Mock(side_effect=Exception)
    monkeypatch.setattr('src.requests_code.requests.get', mock_get)
    yield mock_get


def test_get_post(context):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = get_posts(url)
    assert response.status_code == 200
    assert response.json()["userId"] == 1
    assert response.json()["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"


def test_get_post_exception(context_exception):
    with pytest.raises(Exception, match="Error occurred during get operation"):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        get_posts(url)