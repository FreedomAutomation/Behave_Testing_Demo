Feature: Login and Logout Functionality

  Scenario: Successful Login
    Given the user is on the login page
    When they provide valid credentials
    Then they should be successfully logged in

  Scenario: Logout After Successful Login
    Given the user is logged in
    When they perform logout
    Then they should be redirected to the login page

  Scenario: Click Back Button After Logout
    Given the user is logged in
    When they perform logout
    And they click back button in the browser
    Then they should be redirected to the login page
    And they could not access dashboard error displayed

  Scenario: Login with Invalid Username
    Given the user is on the login page
    When they provide an invalid username
    Then an error message should be displayed

  Scenario: Login with Invalid Password
    Given the user is on the login page
    When they provide an invalid password
    Then an error message should be displayed

  Scenario: Login with Locked User
    Given the user is on the login page
    When they enter locked user credentials
    Then an error message for locked user should be displayed

  Scenario: Login with Both Fields Empty
    Given the user is on the login page
    When they attempt to log in without providing any credentials
    Then an error message for empty credentials should be displayed
