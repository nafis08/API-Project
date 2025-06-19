import requests
from loginData import login_data

print(login_data())
token_data = requests.post('https://restful-booker.herokuapp.com/auth',
                            verify=False,
                            json=login_data(),
                            headers={'Content-Type': 'application/json'})

print(token_data.status_code)
print(token_data.json())
auth_token = token_data.json()['token']