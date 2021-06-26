import requests


def create_ya_folder(folder):
    ya_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    params = {'path': folder}
    ya_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    response = requests.put(ya_url, headers=ya_headers, params=params)
    return response.status_code


token = 'AQAADqwA'
