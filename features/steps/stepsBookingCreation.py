import requests
from behave import *

from booking_creation_payload import booking_creation_payload
from util_package.config import *

# Load configuration for API base URL
config = getConfig()
BASE_URL = config['API']['base_url']

@given('The booking API is available')
def step_impl(context):
    response = requests.get(BASE_URL + "/ping", verify=False)
    assert response.status_code in (200, 201)


@when('I create a booking with the following details')
def step_impl(context):
    # Parse Gherkin table into a flat dictionary
    booking_data = {row['Fields']: row['Values'] for row in context.table}

    # Build final payload, nesting checkin/checkout under bookingdates
    booking_payload = {
        "firstname": booking_data.get("firstName"),
        "lastname": booking_data.get("lastName"),
        "totalprice": float(booking_data.get("totalPrice")),
        "depositpaid": booking_data.get("depositPaid").lower() == "true",
        "bookingdates": {
            "checkin": booking_data.get("checkin"),
            "checkout": booking_data.get("checkout")
        },
        "additionalneeds": booking_data.get("additionalNeeds")
    }

    response = requests.post(
        BASE_URL + "/booking",
        verify=False,
        json=booking_payload,
        headers={"Content-Type": "application/json", "Accept": "application/json"}
    )

    context.response = response
    context.response_data = response.json()
    context.booking_id = context.response_data.get("bookingid")

def getBookingId(context):
    return context.booking_id


@then('The booking should be created successfully')
def step_impl(context):
    assert context.response.status_code in (200, 201)
    assert "bookingid" in context.response_data
    print(f"Booking created successfully with ID: {context.response_data['bookingid']}")


@when('I create a booking with the following details {firstName}, {lastName}, {totalPrice}, {depositPaid}, {checkin}, {checkout} and {additionalNeeds}')
def step_impl(context, firstName, lastName, totalPrice, depositPaid, checkin, checkout, additionalNeeds):
    context.url = BASE_URL + "/booking"
    context.headers = {"Content-Type": "application/json", "Accept": "application/json"}
    context.payload = booking_creation_payload(firstName, lastName, totalPrice, depositPaid, checkin, checkout, additionalNeeds)

    response_multi = requests.post(
        context.url,
        verify=False,
        json=context.payload,
        headers=context.headers
    )

    context.response_multi = response_multi
    context.response_multi_data = response_multi.json()
    context.booking_id = context.response_multi_data.get("bookingid")

@then('All the bookings should be created successfully')
def step_impl(context):
    assert context.response_multi.status_code in (200, 201)
    assert "bookingid" in context.response_multi_data
    print(f"Booking created successfully with ID: {context.response_multi_data['bookingid']}")
    context.booking_id = context.response_multi_data['bookingid']