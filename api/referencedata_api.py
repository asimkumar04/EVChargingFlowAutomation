from api.base_api import BaseClient

class ReferenceDataAPI(BaseClient):
    def get_reference_data(self):
        return self.get("/referencedata/")