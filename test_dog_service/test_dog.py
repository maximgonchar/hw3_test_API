import random
import uuid
import requests
import pytest
import cerberus
from jsonschema import validate

path_list_all_breeds = '/breeds/list/all'
path_random_image = '/breeds/image/random'


class TestDogService:
    def test_list_all_breeds_status(self, base_url):
        res = requests.get(base_url + '/breeds/list/all')
        assert res.status_code == 200

    def test_not_found_list_all_breeds(self, base_url):
        res = requests.get(base_url + '/' + str(uuid.uuid4()))
        assert res.status_code == 404

    def test_get_random_image_status(self, base_url):
        res = requests.get(base_url + '/breeds/image/random')
        assert res.status_code == 200

    def test_api_json_schema_one_dog(self, base_url):
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

    def test_api_json_schema_cerberus_one_dog(self, base_url):
        """Проверка структуры ответа на запрос получения рандомного фото собаки при помощи cerberus"""
        res = requests.get(base_url + '/breeds/image/random').json()
        schema = {
            "message": {"type": "string"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res, schema)
        assert res['status'] == 'success'

    def test_api_json_schema_cerberus_multiply_breed(self, base_url):
        """Проверка структуры ответа на запрос получения рандомного фото нескольких собак"""
        random_dog = random.randint(1, 50)
        res = requests.get(base_url + '/breeds/image/random/' + str(random_dog)).json()
        schema = {
            "message": {"type": "list"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res, schema)
        assert res['status'] == 'success'
        assert len(res['message']) == random_dog
