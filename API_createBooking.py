import requests
import configparser
from booking_creation import booking_creation
from util_package.config import *

config = getConfig()
# Create a new booking using the API
add_booking = requests.post(config['API']['base_url'] + '/booking',
                            verify=False,
                            json=booking_creation(),
                            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, )

#print(type(add_booking))
response_json = add_booking.json()
print(add_booking.json())
#print(add_booking.status_code)
#print(type(response_json))

booking_id = response_json['bookingid']
