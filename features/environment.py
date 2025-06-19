import requests

from booking_creation_payload import booking_creation_payload
from loginData import login_data
from util_package.config import getConfig

config = getConfig()
BASE_URL = config['API']['base_url']


def before_scenario(context, scenario):
    if "dependent" in scenario.tags:
        # Create a new token for authentication
        token_data = requests.post(BASE_URL + '/auth',
                                   verify=False,
                                   json=login_data(),
                                   headers={'Content-Type': 'application/json'})

        print(token_data.status_code)
        print(token_data.json())
        context.auth_token = token_data.json()['token']

        # Create a new booking using the API
        booking_payload = booking_creation_payload('John', 'Doe', 100, True, '2023-10-01', '2023-10-05', 'Breakfast')
        add_booking = requests.post(BASE_URL + '/booking',
                                    verify=False,
                                    json=booking_payload,
                                    headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, )
        context.booking_id_from_env = add_booking.json()['bookingid']
        print(context.booking_id_from_env)
