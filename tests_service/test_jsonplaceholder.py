import pytest
import requests

url_jsonplaceholder = 'https://jsonplaceholder.typicode.com/posts'


class TestJsonPlaceholder:
    def test_get_list_all_resources(self, listing_all_resources_plhr):
        assert len(listing_all_resources_plhr) > 0

    def test_status_all_resources(self, status_code_all_resources_plhr):
        assert status_code_all_resources_plhr == 200

    def test_creating_resorce(self, creating_resouces_plhr):
        assert creating_resouces_plhr['title'] == 'max_g'
        assert creating_resouces_plhr['body'] == 'qa_test'
        assert creating_resouces_plhr['userId'] == '200'

    @pytest.mark.parametrize('input_id, output_id',
                             [(250, '250'),
                              (10, '10'),
                              (0, '0')])
    @pytest.mark.parametrize('input_title, output_title',
                             [('max_title', 'max_title'),
                              ('', ''),
                              (100, '100'),
                              ('$', '$')])
    @pytest.mark.parametrize('input_body, output_body',
                             [('qa_test', 'qa_test'),
                              ('30', '30'),
                              (1, '1'),
                              ('JSON_b', 'JSON_b')])
    def test_post_param_creating_resources(self, input_id, output_id, input_title, output_title, input_body,
                                           output_body):
        res = requests.post(
            url_jsonplaceholder,
            data={'title': input_title, 'body': input_body, 'userId': input_id})
        res_json = res.json()
        assert res_json['title'] == output_title
        assert res_json['body'] == output_body
        assert res_json['userId'] == output_id

    def test_deleting_resouces(self, deleting_resources_plhr):
        assert deleting_resources_plhr == 200
