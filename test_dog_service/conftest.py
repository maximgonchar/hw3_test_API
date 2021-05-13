import cerberus
import pytest
import requests

url_random_image_from_all_dogs = 'https://dog.ceo/api/breeds/image/random'


@pytest.fixture()
def status_response_random_dog_image():
    """Возвращает текст из ответа в status"""
    resp = requests.get(url_random_image_from_all_dogs).json()["status"]
    return resp


@pytest.fixture()
def status_code_random_dog_image():
    """Возвращает код ответа выполнении get запроса на корректный урл"""
    resp = requests.get(url_random_image_from_all_dogs).status_code
    return resp


@pytest.fixture(params=[5, 10, 25, 50])
def status_response_multiply_random_dog(request):
    resp = requests.get(url_random_image_from_all_dogs + '/' + f'{request.param}').json()['status']
    return resp


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://dog.ceo/api",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")

