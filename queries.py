from time import sleep
import requests


def local_server(login, password):
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200


def local_nginx(login, password):
    attempts = 3
    for attempt in range(attempts):
        try:
            response = requests.post('http://127.0.0.1:4000/auth',
                                     json={'login': login, 'password': password})
            return response.status_code == 200
        except:
            if attempt <= 2:
                sleep(1)

    return False
