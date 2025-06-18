import requests
from booking_creation import booking_creation

add_booking = requests.post('https://restful-booker.herokuapp.com/booking',
              json=booking_creation(),
              headers={'Content-Type': 'application/json', 'Accept':'application/json'},)

#print(type(add_booking))
response_json = add_booking.json()
#print(add_booking.json())
#print(add_booking.status_code)
#print(type(response_json))

booking_id = response_json['bookingid']


