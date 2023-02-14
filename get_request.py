import requests
from constants import API_KEY


def get_request(url):
    url = url + "&appid=" + API_KEY
    print(url)
    method = "get"
    return requests.request(method, url).json()['list']
