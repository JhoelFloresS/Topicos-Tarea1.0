import http.client
from src.configs.config import env
import json

class BreedRecognitionService:
    def __init__(self):
        self.api_key = env().get("ZYLALABS_API_KEY")

    def predict(self, url_image):
        conn = http.client.HTTPSConnection("zylalabs.com")
        payload = ''
        headers = {
        "Authorization": "Bearer " + self.api_key
        }
        conn.request("POST", "/api/509/dog+breed+classification+api/378/classificate?url=" + url_image, payload, headers)
        res = conn.getresponse()
        data = res.read()
        return json.loads(data)