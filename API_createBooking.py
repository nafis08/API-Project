import requests
import configparser
from booking_creation_payload import booking_creation_payload
from util_package.config import *

config = getConfig()
BASE_URL = config['API']['base_url']
# Create a new booking using the API
add_booking = requests.post(BASE_URL + '/booking',
                            verify=False,
                            json=booking_creation_payload('Nafisa', 'Khan', 100, True, '2023-10-01', '2023-10-05', 'Breakfast'),
                            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, )

#print(type(add_booking))
response_json = add_booking.json()
print(add_booking.json())
#print(add_booking.status_code)
#print(type(response_json))

booking_id = response_json['bookingid']
