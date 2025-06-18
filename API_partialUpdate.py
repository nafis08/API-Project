from createBooking import booking_id
from bookingPartialUpdate import booking_partial_update
from loginData import auth_util
import requests

partial_update = requests.patch(f'https://restful-booker.herokuapp.com/booking/{booking_id}',
                                json=booking_partial_update(),
                                headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': '5bdfbe5c5c647c0'},
                                auth=(auth_util()))
print(partial_update.status_code)
print(partial_update.json())