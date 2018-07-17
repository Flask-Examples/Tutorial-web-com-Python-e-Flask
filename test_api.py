"""
Test api.

# para executar pytest estrutura de modulo
pytest tests/ -v

# sem estrutura de modulo
# -v informa qual teste foi rodado
pytest test_api.py -v

"""
from app import create_app


def test_api_is_ok():
    app = create_app()
    with app.test_client() as client:
        response = client.get('/api')
        assert response.status_code == 200
        assert 'Bruno' in str(response.data)
        # assert 'ddgdf' in str(response.data)


def test_apiv2_is_ok():
    app = create_app()
    with app.test_client() as client:
        response = client.get('/apiv2')
        assert response.status_code == 200
        assert 'Bruno' in str(response.data)        
