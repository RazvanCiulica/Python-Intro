import requests

def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0 

def test_first_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()

    assert "title" in data[0]
    assert "body" in data[0]

 