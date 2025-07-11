import requests
from loginData import login_data
from util_package.config import getConfig

config = getConfig()
BASE_URL = config['API']['base_url']

print(login_data())
token_data = requests.post(BASE_URL+'/auth',
                            verify=False,
                            json=login_data(),
                            headers={'Content-Type': 'application/json'})

print(token_data.status_code)
print(token_data.json())
auth_token = token_data.json()['token']