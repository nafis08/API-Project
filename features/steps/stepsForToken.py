from behave import *
import requests
from loginData import login_data
from util_package.config import getConfig

config = getConfig()
BASE_URL = config['API']['base_url']

@given('The authentication API is available')
def step_impl(context):
    response = requests.get(BASE_URL + "/ping", verify=False)
    assert response.status_code in (200, 201), f"API is not available, received status code: {response.status_code}"

@when('I create a token with the following details')
def step_impl(context):

    # Ensure the login data is available
    auth_data = {row['Fields']: row['Values'] for row in context.table}
    auth_payload = {
        "username": auth_data.get("username"),
        "password": auth_data.get("password")
    }

    token_data = requests.post(BASE_URL+'/auth',
                               verify=False,
                               json=auth_payload,
                               headers={'Content-Type': 'application/json'})

    context.token_response = token_data
    context.auth_token = token_data.json() #retrieving authentication token from the response

@then('The token should be created successfully')
def step_impl(context):
    assert context.token_response.status_code in (200, 201)
    assert "token" in context.auth_token
    print(f"Token created successfully: {context.auth_token['token']}")
    # Storing token for further use in the test suite
    context.token = context.auth_token['token']

def getToken(context):
    return context.token

@then(f'The token creation should fail with an error message')
def step_impl(context):
    error_message = context.token_response.json().get('reason', 'Bad credentials') # retrieving failure reason from the response
    print(f"Token creation failed with error: {error_message}")
    assert "Bad credentials" in error_message, "Bad credentials"