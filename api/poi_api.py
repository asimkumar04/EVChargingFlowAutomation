from api.base_api import BaseClient

class POIApi(BaseClient):

    def get_poi(self, params=None):
        return self.get("/poi/", params=params)