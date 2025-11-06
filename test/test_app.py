from app import app


def test_home_route():
    """Prueba que la ruta principal responda correctamente."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Hola, soy Jary_Cuji. Proyecto de taller." in response.data
