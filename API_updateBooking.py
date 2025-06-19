from API_createBooking import booking_id
from bookingUpdate import booking_update
from API_tokenCreation import auth_token
from loginData import auth_util
import requests
from util_package.config import *

config = getConfig()

updateBooking = requests.put(config['API']['base_url']+f'/booking/{booking_id}',
                             verify=False,
                             json=booking_update(),
                             headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                      'Cookie': auth_token},
                             auth=(auth_util()),)

print(updateBooking.status_code)
print(updateBooking.json())
