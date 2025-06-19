Feature: Creating token using authentication API

  Scenario: Verify token creation with valid credentials
    Given The authentication API is available
    When I create a token with the following details
      | Fields   | Values      |
      | username | admin       |
      | password | password123 |
    Then The token should be created successfully

  Scenario: Verify token creation with invalid credentials
    Given The authentication API is available
    When I create a token with the following details
      | Fields     | Values       |
      | username   | invalidUser  |
      | password   | wrongPass    |
    Then The token creation should fail with an error message