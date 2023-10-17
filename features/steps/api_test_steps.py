import json
import requests
from behave import given, when, then

headers = {
    "X-RapidAPI-Key": "bb54eb79e0msh9029e67e1a86070p1b43c9jsn9e385df09d95",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
unauthorized_headers = {
    "X-RapidAPI-Key": "incorrect",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
API_ENDPOINT = "https://weatherapi-com.p.rapidapi.com/timezone.json"
NON_EXISTING_RESOURCE = "https://weatherapi-com.p.rapidapi.com/timezine.json"

with open('features/support/test_data/get_request_data.json') as json_data:
    TEST_DATA = json.load(json_data)

@given('the API endpoint for retrieving data')
def step_given_sorted_api_endpoint(context):
    context.api_endpoint = API_ENDPOINT

@given('the API endpoint with non existing resource for retrieving data')
def step_given_sorted_api_endpoint(context):
    context.api_endpoint = NON_EXISTING_RESOURCE

@when('I send a GET request to the endpoint')
def step_when_send_post_request_unauthorized(context):
    # Replace this with your actual payload for an unauthorized POST request
    querystring = TEST_DATA['positive_test_cases']['Valid User Registration']['request_body']
    context.response = requests.get(context.api_endpoint, params=querystring, headers=headers)

@then('the API should respond with a status code of {status_code}')
def step_then_check_status_code(context, status_code):
    expected_status_code = int(status_code)
    assert context.response.status_code == expected_status_code, \
        f"Unexpected status code: {context.response.status_code}, expected: {expected_status_code}"

@then('the response should contain the expected data')
def step_then_check_created_resource_data(context):
    # With mocks we can validate data but for time been this works
    data = TEST_DATA['positive_test_cases']['Valid User Registration']['expected_response']
    assert data['location']['name'] == context.response.json()['location']['name'], "Created resource data not found in the response"
    assert data['location']['region'] == context.response.json()['location']['region'], "Created resource data not found in the response"

@when('I send a GET request with invalid parameters')
def step_when_send_post_request_unauthorized(context):
    # Replace this with your actual payload for an unauthorized POST request
    querystring = TEST_DATA['negative_test_cases']['Invalid Parameter']['request_body']
    context.response = requests.get(context.api_endpoint, params=querystring, headers=headers)

@then('the response should contain an appropriate error message')
def step_then_check_status_code(context):
    data = TEST_DATA['negative_test_cases']['Invalid Parameter']['expected_response']
    assert data == context.response.json()['error'], "Authentication error message not found in the response"

@when('I send a GET request for a non-existent resource')
def step_when_send_post_request_unauthorized(context):
    # Replace this with your actual payload for an unauthorized POST request
    querystring = TEST_DATA['positive_test_cases']['Valid User Registration']['request_body']
    context.response = requests.get(context.api_endpoint, params=querystring, headers=headers)

@when('I send a GET request without proper authorization')
def step_when_send_post_request_unauthorized(context):
    # Replace this with your actual payload for an unauthorized POST request
    querystring = TEST_DATA['positive_test_cases']['Valid User Registration']['request_body']
    context.response = requests.get(context.api_endpoint, params=querystring, headers=unauthorized_headers)

@then('the response should contain an authentication error message')
def step_then_check_authentication_error(context):
    # Replace this with your actual validation logic based on the expected authentication error message
    assert 'You are not subscribed to this API.' in context.response.json()['message'], "Authentication error message not found in the response"
