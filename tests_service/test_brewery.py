import cerberus
from jsonschema import validate, ValidationError


class TestBreweries:
    def test_get_list_all_breweries(self, list_breweries):
        assert len(list_breweries) > 0

    def test_status_all_breweries(self, status_code_breweries):
        assert status_code_breweries == 200

    def test_brew_by_city(self, response_brew_by_city):
        assert response_brew_by_city[0]['city'] == 'San Diego'
        assert response_brew_by_city[0]['state'] == 'California'

    def test_brew_by_name(self, response_brew_by_name):
        assert response_brew_by_name[0]['name'] == 'Ironbark Brewery'

    def test_brew_by_state(self, response_brew_by_state):
        assert response_brew_by_state[0]['state'] == 'Ohio'

    def test_brew_by_type(self, response_brew_by_type):
        assert response_brew_by_type[0]['brewery_type'] == 'large'

    def test_json_schema_brew_by_id(self, response_brew_by_id_schema):
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "obdb_id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            },
            "required": ["id", "obdb_id", "name", "state", "country", "created_at", "postal_code"]
        }
        validate(instance=response_brew_by_id_schema, schema=schema)
        assert len(response_brew_by_id_schema) > 0


