class TestJsonPlaceholder:
    def test_get_list_all_resources(self, listing_all_resources):
        assert len(listing_all_resources) > 0

    def test_status_all_resources(self, status_code_all_resources):
        assert len(status_code_all_resources) == 200