from behave import given, when, then
from features.support.web_library.LoginPage import LoginPage
from features.support.web_library.DashboardPage import DashboardPage


STANDARD_USER = 'standard_user'
LOCKED_OUT_USER = 'locked_out_user'
NON_EXISTING_USER = 'non_existing_user'
VALID_PASSWORD = 'secret_sauce'
INVALID_PASSWORD = 'invalid_password'
ERROR_MESSAGE_FOR_INVALID_USER = "Epic sadface: Username and password do not match any user in this service"
ERROR_MESSAGE_FOR_LOCKED_OUT_USER = "Epic sadface: Sorry, this user has been locked out"
ERROR_MESSAGE_FOR_EMPTY_CREDENTIALS = "Epic sadface: Username is required"
ERROR_MESSAGE_FOR_BACK_BUTTON_AFTER_LOGOUT = "Epic sadface: You can only access '/inventory.html' when you are logged in."

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('they provide valid credentials')
def step_when_provide_valid_credentials(context):
    context.login_page.login(username=STANDARD_USER, password=VALID_PASSWORD)

@then('they should be successfully logged in')
def step_then_successful_login(context):
    assert context.login_page.is_logged_in()

@given('the user is logged in')
def step_given_user_logged_in(context):
    # Simulate a user being logged in for the next scenario
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    context.login_page.login(username=STANDARD_USER, password=VALID_PASSWORD)
    context.dashboard_page = DashboardPage(context.driver)

@when('they perform logout')
def step_when_perform_logout(context):
    context.dashboard_page.logout()

@then('they should be redirected to the login page')
def step_then_redirected_to_login_page(context):
    assert context.dashboard_page.is_redirected_to_login()

@when('they click back button in the browser')
def step_when_perform_logout(context):
    context.dashboard_page.click_back_button()

@then('they could not access dashboard error displayed')
def step_then_redirected_to_login_page(context):
    assert context.login_page.error_message_displayed(ERROR_MESSAGE_FOR_BACK_BUTTON_AFTER_LOGOUT)

@when('they provide an invalid username')
def step_when_provide_invalid_username(context):
    context.login_page.login(username=NON_EXISTING_USER, password=VALID_PASSWORD)

@when('they provide an invalid password')
def step_when_provide_invalid_password(context):
    context.login_page.login(username=STANDARD_USER, password=INVALID_PASSWORD)

@when('they attempt to log in without providing any credentials')
def step_when_attempt_login_with_empty_fields(context):
    context.login_page.login(username='', password='')

@when('they enter locked user credentials')
def step_when_attempt_login_with_empty_fields(context):
    context.login_page.login(username=LOCKED_OUT_USER, password=VALID_PASSWORD)

@then('an error message should be displayed')
def step_then_error_message_displayed(context):
    assert context.login_page.error_message_displayed(ERROR_MESSAGE_FOR_INVALID_USER)

@then('an error message for empty credentials should be displayed')
def step_then_error_message_displayed(context):
    assert context.login_page.error_message_displayed(ERROR_MESSAGE_FOR_EMPTY_CREDENTIALS)

@then('an error message for locked user should be displayed')
def step_then_error_message_displayed(context):
    assert context.login_page.error_message_displayed(ERROR_MESSAGE_FOR_LOCKED_OUT_USER)

@then('an error message should not be displayed')
def step_then_error_message_not_displayed(context):
    assert context.login_page.error_message_is_not_displayed()
