import requests
from constants import API_KEY
from requests.auth import HTTPBasicAuth


def get_request(url):
    url = url + "&appid=" + API_KEY
    print(url)
    # params = dict(key=API_KEY)
    # return requests.get(url, params=params).json()
    method = "get"
    # auth = HTTPBasicAuth(API_KEY, secret)
    # headers = {
    #     'Content-type': 'application/json',
    #     'Authorization': f'ApiKey {API_KEY}'
    # }

    return requests.request(method, url).json()['list']
