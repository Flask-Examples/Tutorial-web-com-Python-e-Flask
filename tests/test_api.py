"""
Test api.

# para executar pytest
pytest tests/ -v

"""


def test_api_is_ok(app):
    with app.test_client() as client:
        response = client.get('/api')
        assert response.status_code == 200
        assert 'Bruno' in str(response.data)
