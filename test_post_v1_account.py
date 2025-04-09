import requests


json_data = {
    'login': 'test@test.ru',
    'email': 'test@test.ru',
    'password': '123456',
}

response = requests.post('http://5.63.153.31:5051/v1/account', json=json_data)
