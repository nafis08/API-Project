import json
import requests
from API_createBooking import booking_id
from API_tokenCreation import auth_token
from loginData import auth_util
from util_package.config import *

config = getConfig()

print(booking_id)
delete_booking = requests.delete(config['API']['base_url']+f'/booking/{booking_id}',
                                 verify=False,
                                 headers={'Cookie': auth_token}, auth=(auth_util()))
print(delete_booking.text)
print(delete_booking.status_code)