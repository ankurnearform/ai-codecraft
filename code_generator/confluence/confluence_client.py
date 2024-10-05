import requests
class ConfluenceClient:
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth = auth_token

    def fetch_page(self, page_id):
        url = f"{self.base_url}/wiki/rest/api/content/{page_id}?expand=body.storage"
        headers = {'Authorization': f'Bearer {self.auth}'}
        response = requests.get(url, headers=headers)
        return response.json()['body']['storage']['value']
