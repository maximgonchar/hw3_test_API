import requests
import cerberus
from jsonschema import validate
import pytest

path_list_all_breeds = '/breeds/list/all'
path_random_image = '/breeds/image/random'


class TestApiDog:

    def test_status_random_dog(self, status_response_random_dog_image):
        assert status_response_random_dog_image == 'success'

    def test_status_code_random_dog(self, status_code_random_dog_image):
        assert status_code_random_dog_image == 200

    def test_status_multiply_random_dog(self, response_multiply_random_dog):
        assert response_multiply_random_dog['status'] == 'success'

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

    def test_api_multiply_random_dogs(self, response_multiply_random_dog):
        """Проверка структуры ответа запроса рандомного списка нескольких собак через cerberus"""
        schema = {
            "message": {"type": "list"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(response_multiply_random_dog, schema)

    def test_single_random_image_from_a_sub_breed_from_breed(self, dog_sub_breed_from_breed):
        assert dog_sub_breed_from_breed == 'success'

    @pytest.mark.parametrize("count_dogs", [x for x in range(2, 5)])
    @pytest.mark.parametrize("breeds", ["terrier", "spaniel", "hound", "vizsla"])
    def test_api_multiply_random_dogs(self, base_url, count_dogs, breeds):
        """Проверка рандомного фото нескольких собак"""
        res = requests.get(base_url + f'/breed/{breeds}/images/random/{count_dogs}')
        schema = {
            "message": {"type": "list"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        print(len(res.json()['message']))
        assert v.validate(res.json(), schema)
        assert len(res.json()['message']) == count_dogs
