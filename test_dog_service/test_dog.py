import random
import uuid
import requests
import pytest
import cerberus
from jsonschema import validate

path_list_all_breeds = '/breeds/list/all'
path_random_image = '/breeds/image/random'


class TestDogService:
    def test_list_all_breeds(self, base_url):
        res = requests.get(base_url + path_list_all_breeds)
        assert res.status_code == 200

    def test_no_list_all_breeds(self, base_url):
        res = requests.get(base_url + '/' + str(uuid.uuid4()))
        assert res.status_code == 404

    def test_get_random_image(self, base_url):
        res = requests.get(base_url + path_random_image)
        assert res.status_code == 200

    def test_api_json_schema(self, base_url):
        """Проверка структуры ответа на запрос получения рандомного фото собаки"""
        res = requests.get(base_url + path_random_image)
        schema = {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "status": {"type": "string"}
            },
            "required": ["message", "status"]
        }
        assert validate(instance=res.json(), schema=schema) == None

    def test_api_json_schema_cerberus(self, base_url):
        """Проверка структуры ответа на запрос получения рандомного фото собаки при помощи cerberus"""
        res = requests.get(base_url + path_random_image)
        schema = {
            "message": {"type": "string"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res.json(), schema)

    def test_api_json_schema_cerberus_multiply_breed(self, base_url):
        """Проверка структуры ответа на запрос получения рандомного фото нескольких собак"""
        res = requests.get(base_url + path_random_image + '/' + str(random.randint(1, 50)))
        schema = {
            "message": {"type": "list"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res.json(), schema)
