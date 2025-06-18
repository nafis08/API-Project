import json
import requests
from createBooking import add_booking
from API_tokenCreation import auth_token
from loginData import auth_util

print(add_booking.json()['bookingid'])
delete_booking = requests.delete(f'https://restful-booker.herokuapp.com/booking/{add_booking.json()["bookingid"]}',
                                 headers={'Cookie': auth_token}, auth=(auth_util()))
print(delete_booking.text)
print(delete_booking.status_code)