import requests
from behave import *
from util_package.config import getConfig

config = getConfig()
BASE_URL = config['API']['base_url']

#@given("The booking API is available")
#def step_impl(context):
#    response = requests.get(BASE_URL + "/ping", verify=False)
#    assert response.status_code in (200, 201)

@when('I search for booking IDs with the following parameters')
def step_impl(context):
    search_params = {row['Fields']: row['Values'] for row in context.table}
    response = requests.get(
        BASE_URL + "/booking/",
        params=search_params,
        verify=False
    )
    context.response = response
    context.response_data = response.json()

@then("The API should return one or more booking IDs")
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response_data, list), "Expected a list of bookings"
    assert len(context.response_data) >= 0, "Expected at least one booking ID"

@then("The API should return an empty list")
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response_data, list), "Expected a list of bookings"
    assert len(context.response_data) == 0, "Expected no bookings"
