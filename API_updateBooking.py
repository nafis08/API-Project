from createBooking import add_booking
from bookingUpdate import booking_update
from API_tokenCreation import auth_token
from loginData import auth_util
import requests

updateBooking = requests.put(f'https://restful-booker.herokuapp.com/booking/{add_booking.json()["bookingid"]}',
                             json=booking_update(),
                             headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                      'Cookie': auth_token},
                             auth=(auth_util()),)

print(updateBooking.status_code)
print(updateBooking.json())
