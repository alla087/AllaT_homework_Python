import pytest
import requests

# Токен авторизации, который нужно будет заменить
AUTH_TOKEN = "вставить свой пароль"

# Базовый URL для API
BASE_URL = "https://ru.yougile.com/api-v2"

# Заголовки с авторизацией
HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

# Пример позитивного теста для метода POST
@pytest.mark.parametrize("project_name", ["Test Project", "Another Project"])
def test_create_project_positive(project_name):
    response = requests.post(f"{BASE_URL}/projects", headers=HEADERS, json={"title": project_name})
    assert response.status_code == 201
    assert "id" in response.json()

# Пример негативного теста для метода POST
@pytest.mark.parametrize("invalid_data", [None, "", 123])
def test_create_project_negative(invalid_data):
    response = requests.post(f"{BASE_URL}/projects", headers=HEADERS, json={"titleв": invalid_data})
    assert response.status_code == 400


# Пример позитивного теста для метода GET
@pytest.mark.parametrize("project_name", ["Test Project", "Another Project"])
def test_get_project_success(project_name):
    response_create = requests.post(f"{BASE_URL}/projects", headers=HEADERS, json={"title": project_name})
    id_project = response_create.json()["id"]
    response = requests.get(f"{BASE_URL}/projects/{id_project}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["title"] == project_name

# Пример негативного теста для метода GET
def test_get_project_not_found():
# Проверяем, что запрос на несуществующий проект возвращает ошибку
    response = requests.get(f"{BASE_URL}/projects/7", headers=HEADERS)
    assert response.status_code == 404

# Пример позитивного теста для метода PUT
def test_put_project_success():
    response_create = requests.post(f"{BASE_URL}/projects", headers=HEADERS, json={"title": "Test Project"})
    id_project = response_create.json()["id"]
    data = {
        "title": "Updated Project Name"
        }
    response = requests.put(f"{BASE_URL}/projects/{id_project}", headers=HEADERS, json=data)
    assert response.status_code == 200

# Пример негативного теста для метода PUT
def test_put_project_failure():
    id_project = 9999  # Предполагаем, что проект с таким ID не существует
    data = {
        "title": "Updated Project Name"
    }
    response = requests.put(f"{BASE_URL}/projects/{id_project}", headers=HEADERS, json=data)
    assert response.status_code == 404  # Ожидаем, что сервер вернет ошибку