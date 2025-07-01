from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_health_route():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
