import requests

class BaseClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get(self, endpoint, params=None):
        if params is None:
            params = {}

        # OpenChargeMap requires api_key as query param
        params["key"] = self.api_key

        return requests.get(f"{self.base_url}{endpoint}", params=params)