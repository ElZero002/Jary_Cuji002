# test_app.py
from app import app

def test_home_route():
    # Simula una petición al servidor Flask
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Hola" in response.data  # verifica que devuelva algo de texto
