import requests


class BaseAPI:
    def __init__(self, env_class):
        self.__base_url = env_class.base_api_url
        self.__headers = {'Accept': '*/*', 'Content-Type': 'application/json', 'Cookie': 'token=abc123',
                          'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}
        self.__request = requests

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f"{self.__base_url}{url}", headers=headers)
        return response

    def post(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.post(f"{self.__base_url}{url}", json=body, headers=headers)
        return response

    def put(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.put(f"{self.__base_url}{url}", json=body, headers=headers)
        return response

    def patch(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.patch(f"{self.__base_url}{url}", json=body, headers=headers)
        return response

    def delete(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.delete(f"{self.__base_url}{url}", headers=headers)
        return response
