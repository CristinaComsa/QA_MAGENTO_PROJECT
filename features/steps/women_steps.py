import time
from behave import *


@then('I click on tops category')
def step_impl(context):
    time.sleep(3)
    context.women_page.click_on_tops()


@then('I should be on tops category items page')
def step_impl(context):
    time.sleep(3)
    context.women_page.is_tops_page(), 'url is incorrect'


@then('I expected to be 13 shopping categories')
def step_impl(context):
    assert context.women_page.get_shopping_categories() == 13, "different categories"


@then('I expected to be 50 items')
def step_impl(context):
    assert context.women_page.get_amount_items() == "50", "different quantity"


@then('I select sort by price')
def step_impl(context):
    context.women_page.click_on_price()


@then('items should be on ascending order')
def step_impl(context):
    context.women_page.is_ascending_price(), 'url is incorrect'


@then('items should be on descending order')
def step_impl(context):
    context.women_page.click_on_descending_arrow()
    context.women_page.is_descending_price(), 'url is incorrect'


@then('I click on the "LUMA" icon')
def step_impl(context):
    context.women_page.click_on_logo()


@then('I should be on the home page')
def step_impl(context):
    context.women_page.is_home_page(), 'is not home page :('
