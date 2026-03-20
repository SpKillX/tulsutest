import requests
import pytest

def test_go_http_server():
    url = "http://localhost:8080/hello"
    try:
        response = requests.get(url, timeout=5)
        assert response.status_code == 200
        assert "Сервер на Go." in response.text
    except requests.exceptions.ConnectionError:
        pytest.fail("Сервер Go не запущен на порту 8080. Запустите его перед тестом.")


test_go_http_server()