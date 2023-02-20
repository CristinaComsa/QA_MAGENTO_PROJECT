import time
from behave import *


@when('I click on sign in button')
def step_impl(context):
    context.login_page.click_on_sign_in_button()
    time.sleep(3)


@when('the Customer login message appear')
def step_impl(context):
    text = context.login_page.get_customer_message()
    assert "Customer Login" in text, 'message not found'
    time.sleep(3)


@when('I input a "{email}" username')
def step_impl(context, email):
    context.login_page.enter_email(email)
    time.sleep(2)


@when('I input a "{password}" password')
def step_impl(context, password):
    context.login_page.enter_password(password)
    time.sleep(2)


@when('I click on sign in')
def step_impl(context):
    context.login_page.sign_in()
    time.sleep(3)


@then('I should be logged in to my account')
def step_impl(context):
    message = context.login_page.get_welcome_message()
    assert "Welcome" in message, 'message not displayed'


@given('I Am successful logged in')
def step_impl(context):
    message = context.login_page.get_welcome_message()
    assert "Welcome" in message, 'message not displayed'


@when('I click on my account button to go on the user menu page')
def step_impl(context):
    context.login_page.logout_button()


@when('On the user menu page I click the Sign out button')
def step_impl(context):
    context.login_page.logout()


@then('I don\'t find the username on the main page')
def step_impl(context):
    message = context.home_page.get_home_message()
    assert "This is a demo store. No orders will be fulfilled" in message, 'message not displayed'


@then('the "Customer Login" still appear')
def step_impl(context):
    message = context.login_page.get_customer_login_message()
    time.sleep(3)
    assert "Customer Login" in message, 'message not displayed'


@when('I enter "cristina_comsa@yahoo.com" and a "cristina2023@"')
def step_impl(context):
    print('STEP: When I enter "cristina_comsa@yahoo.com" and a "cristina2023@"')
