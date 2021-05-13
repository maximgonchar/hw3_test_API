import random
import uuid
import requests
import pytest
import cerberus
from jsonschema import validate

path_list_all_breeds = '/breeds/list/all'
path_random_image = '/breeds/image/random'


class TestDogService:


    def test_not_found_list_all_breeds(self, base_url):
        res = requests.get(base_url + '/' + str(uuid.uuid4()))
        assert res.status_code == 404

    def test_get_random_image_status(self, base_url):
        res = requests.get(base_url + '/breeds/image/random')
        assert res.status_code == 200

    def test_api_json_schema_random_dog(self, base_url):
        """Проверка структуры ответа на запрос получения рандомного фото собаки"""
        res = requests.get(base_url + '/breeds/image/random').json()
        schema = {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "status": {"type": "string"}
            },
            "required": ["message", "status"]
        }
        validate(instance=res, schema=schema)
        assert res['status'] == 'success'

    def test_api_json_schema_cerberus_random_dog(self, base_url):
        """Проверка структуры ответа на запрос получения рандомного фото собаки при помощи cerberus"""
        res = requests.get(base_url + '/breeds/image/random').json()
        schema = {
            "message": {"type": "string"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res, schema)
        assert res['status'] == 'success'

    # def test_api_json_schema_cerberus_random_dogs(self, base_url):
    #     """Проверка структуры ответа на запрос получения рандомного фото нескольких собак"""
    #     random_dog = random.randint(1, 50)
    #     res = requests.get(base_url + '/breeds/image/random/' + str(random_dog)).json()
    #     schema = {
    #         "message": {"type": "list"},
    #         "status": {"type": "string"}
    #     }
    #     v = cerberus.Validator()
    #     assert v.validate(res, schema)
    #     assert res['status'] == 'success'
    #     assert len(res['message']) == random_dog

    @pytest.mark.parametrize("count_dogs", [x for x in range(1, 51)])
    def test_api_multiply_random_from_all_dogs(self, base_url, count_dogs):
        """Проверка структуры ответа, статус-кода на запрос получения рандомного фото нескольких собак"""
        res = requests.get(base_url + f'/breeds/image/random/{count_dogs}')
        schema = {
            "message": {"type": "list"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res.json(), schema)
        assert res.json()['status'] == 'success'
        assert len(res.json()['message']) == count_dogs
        assert res.status_code == 200

    @pytest.mark.parametrize("count_dogs", [x for x in range(1, 51)])
    def test_api_multiply_random_dogs(self, base_url, count_dogs):
        """Проверка структуры ответа, статус-кода на запрос получения рандомного фото нескольких собак"""
        res = requests.get(base_url + f'/breed/hound/images/random/{count_dogs}')
        schema = {
            "message": {"type": "list"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res.json(), schema)
        assert res.json()['status'] == 'success'
        assert len(res.json()['message']) == count_dogs
        assert res.status_code == 200

    def test_api_all_dog_from_breed_collection(self, base_url):
        res = requests.get(base_url + '/breed/hound/images')
        print(len(res.json()['message']))


class TestApiDog:
    def test_status_random_dog(self, status_response_random_dog_image):
        assert status_response_random_dog_image == 'success'

    def test_status_code_random_dog(self, status_code_random_dog_image):
        assert status_code_random_dog_image == 200

    def test_status_multiply_random_dog(self, status_response_multiply_random_dog):
        assert status_response_multiply_random_dog == 'success'


