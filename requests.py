import requests
import json

class Request:
    def __init__(self):
        self._header = headers

    def getcontent(url, param):
        response = requests.get(url, headers = headers, params = param)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            print(f"Error in completing request. Response code : {response.status_code}")
            return None