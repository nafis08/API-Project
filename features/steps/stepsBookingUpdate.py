import requests
from behave import *

from booking_creation_payload import booking_creation_payload
from util_package.config import *

# Load configuration for API base URL
config = getConfig()
BASE_URL = config['API']['base_url']


@given('The booking API for update is available')
def step_impl(context):
    response = requests.get(BASE_URL + "/ping", verify=False)
    assert response.status_code in (200, 201)


@when('I update a booking with the parameters {firstName}, {lastName}, {totalPrice}, {checkin}, {checkout}, {depositPaid}, {additionalNeeds}')
def step_impl(context, firstName, lastName, totalPrice, checkin, checkout, depositPaid, additionalNeeds):
    booking_payload = booking_creation_payload(firstName, lastName, totalPrice, checkin, checkout, depositPaid, additionalNeeds)

    context.response = requests.put(
        BASE_URL + f"/booking/{context.booking_id_from_env}",
        verify=False,
        json=booking_payload,
        headers={"Content-Type": "application/json", "Accept": "application/json", "Cookie": context.auth_token},
        auth=('admin', 'password123')  # Replace with actual auth if needed
    )


@then('The booking should be updated successfully with the given parameters')
def step_impl(context):
    assert context.response.status_code in (200, 201)
