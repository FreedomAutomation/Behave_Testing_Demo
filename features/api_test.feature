Feature: Testing GET Endpoint

  Scenario: Positive Test - Retrieve Data
    Given the API endpoint for retrieving data
    When I send a GET request to the endpoint
    Then the API should respond with a status code of 200
    And the response should contain the expected data

  Scenario: Negative Test - Invalid Parameters
    Given the API endpoint for retrieving data
    When I send a GET request with invalid parameters
    Then the API should respond with a status code of 400
    And the response should contain an appropriate error message

  Scenario: Negative Test - Resource Not Found
    Given the API endpoint with non existing resource for retrieving data
    When I send a GET request for a non-existent resource
    Then the API should respond with a status code of 404

  Scenario: Negative Test - Unauthorized Access
    Given the API endpoint for retrieving data
    When I send a GET request without proper authorization
    Then the API should respond with a status code of 403
    And the response should contain an authentication error message
