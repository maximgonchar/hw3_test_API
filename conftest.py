import pytest
import requests

url_random_image_from_all_dogs = 'https://dog.ceo/api/breeds/image/random'
url_list_all_sub_breed_from_breed = 'https://dog.ceo/api/breed/'
url_breweries = 'https://api.openbrewerydb.org/breweries'
url_jsonplaceholder = 'https://jsonplaceholder.typicode.com/posts'


@pytest.fixture()
def status_response_random_dog_image():
    """Возвращает текст из ответа в status"""
    resp = requests.get(url_random_image_from_all_dogs).json()
    return resp


@pytest.fixture()
def status_code_random_dog_image():
    """Возвращает код ответа выполнении get запроса на корректный урл"""
    resp = requests.get(url_random_image_from_all_dogs).status_code
    return resp


@pytest.fixture(params=[5, 10, 25, 50])
def response_multiply_random_dog(request):
    """Возвращает json-ответ нескольких собак"""
    resp = requests.get(url_random_image_from_all_dogs + '/' + f'{request.param}').json()
    if len(resp['message']) == request.param:
        return resp
    else:
        return AssertionError


@pytest.fixture(params=["terrier", "spaniel", "hound"])
def dog_sub_breed_from_breed(request):
    """Возвращает статус ответа запроса рандомной суб-породы от указанной породы"""
    response = requests.get(url_list_all_sub_breed_from_breed + f'{request.param}/images/random').json()['status']
    return response


@pytest.fixture()
def list_breweries():
    resp = requests.get(url_breweries).json()
    return resp


@pytest.fixture()
def status_code_breweries():
    resp = requests.get(url_breweries).status_code
    return resp


@pytest.fixture(params=[{"by_city": "san_diego"}])
def response_brew_by_city(request):
    resp = requests.get(url_breweries, params=request.param).json()
    return resp


@pytest.fixture(params=[{"by_name": "Ironbark Brewery"}])
def response_brew_by_name(request):
    resp = requests.get(url_breweries, params=request.param).json()
    return resp


@pytest.fixture(params=[{"by_state": "ohio"}])
def response_brew_by_state(request):
    resp = requests.get(url_breweries, params=request.param).json()
    return resp


@pytest.fixture(params=[{"by_type": "large"}])
def response_brew_by_type(request):
    resp = requests.get(url_breweries, params=request.param).json()
    return resp


@pytest.fixture(params=[9754, 9180, 9094, 9180, 9754, 10217])
def response_brew_by_id_schema(request):
    resp = requests.get(url_breweries + '/' + f'{request.param}').json()
    return resp


@pytest.fixture()
def listing_all_resources_plhr():
    resp = requests.get(url_jsonplaceholder).json()
    return resp


@pytest.fixture()
def status_code_all_resources_plhr():
    resp = requests.get(url_jsonplaceholder).status_code
    return resp


@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7])
def response_getting_resources_plhr(request):
    resp = requests.get(url_jsonplaceholder + '/' + f'{request.param}').json()
    return resp


@pytest.fixture()
def creating_resouces_plhr():
    payload = {'title': 'max_g',
               'body': 'qa_test',
               'userId': 200, }
    resp = requests.post(url_jsonplaceholder, data=payload)
    resp_json = resp.json()
    return resp_json


@pytest.fixture(params=[0, 10, 200, 250])
def deleting_resources_plhr(request):
    resp = requests.delete(url_jsonplaceholder + '/' + f'{request.param}').status_code
    return resp


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action='store',
        help="Укажите ссылку",
        default="https://ya.ru"
    )

    parser.addoption(
        "--status_code",
        help="Передайте код ошибки",
        default="200"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def response_code(request):
    return request.config.getoption("--status_code")
