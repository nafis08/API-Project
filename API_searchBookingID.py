import requests

from features.steps.stepsBookingCreation import BASE_URL
from util_package.config import getConfig

config = getConfig()
BASE_URL = config['API']['base_url']

booking_search = requests.get(BASE_URL + f'/booking/',
                                params={'firstname': 'John'},
                                verify=False,
                                headers={'Content-Type': 'application/json'})

print(booking_search.json())
print(type(booking_search.json()))
print(booking_search.status_code)