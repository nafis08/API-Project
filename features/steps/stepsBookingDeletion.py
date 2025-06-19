import requests
from util_package.config import getConfig
from behave import given, when, then

congif = getConfig()
BASE_URL = congif['API']['base_url']


@given('The booking API for deletion is available')
def step_impl(context):
    response = requests.get(BASE_URL + "/ping", verify=False)
    assert response.status_code in (200, 201), f"API is not available, received status code: {response.status_code}"

@when('I delete a booking with the following details')
def step_impl(context):
    # Convert table to dict
    booking_data = {row['Fields']: row['Values'] for row in context.table}

    # Replace placeholder with real booking ID from context
    if booking_data['bookingId'] == 'validBookingId':
        booking_id = context.booking_id_from_env
    else:
        booking_id = booking_data['bookingId']

    response = requests.delete(
        getConfig()['API']['base_url'] + f"/booking/{booking_id}",
        verify=False,
        headers={"Content-Type": "application/json", "Cookie": context.auth_token},
        auth=('admin', 'password123')  # Replace with actual auth if needed

    )
    context.response = response
    context.response_data = response.text if response.status_code == 201 else None

@then('The booking should be deleted successfully')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"
    assert "Created" in context.response_data


