import time
from behave import *


@given('I open Magento page')
def step_impl(context):
    url = 'https://magento.softwaretestingboard.com/'
    context.driver.get(url)
    time.sleep(3)


@given('Magento title is available')
def step_impl(context):
    title = 'Home Page - Magento eCommerce - website to practice selenium | demo website for automation testing |' \
            ' selenium practice sites | selenium demo sites | best website to practice selenium automation |' \
            ' automation practice sites Magento Commerce - website to practice selenium | ' \
            'demo website for automation testing | selenium practice sites'
    assert 'Magento eCommerce' in title, 'title is not correct'


@given('the message "demo store" appear')
def step_impl(context):
    message = context.home_page.get_home_message()
    assert "This is a demo store. No orders will be fulfilled" in message


@when('I click on what\'s new button')
def step_impl(context):
    context.home_page.click_on_new_products()


@then('I should be on what\'s new section')
def step_impl(context):
    assert context.home_page.is_new_products_page(), 'url is incorrect'


@when('I click on women button')
def step_impl(context):
    context.home_page.click_on_women_products()


@then('I should be on women section')
def step_impl(context):
    assert context.home_page.is_women_products_page(), 'url is incorrect'


@when('I click on men button')
def step_impl(context):
    context.home_page.click_on_men_products()


@then('I should be on men section')
def step_impl(context):
    assert context.home_page.is_men_products_page(), 'url is incorrect'


@when('I click on gear button')
def step_impl(context):
    context.home_page.click_on_gear_products()


@then('I should be on gear section')
def step_impl(context):
    assert context.home_page.is_gear_products_page(), 'url is incorrect'


@when('I click on training button')
def step_impl(context):
    context.home_page.click_on_training_products()


@then('I should be on training section')
def step_impl(context):
    assert context.home_page.is_training_products_page(), 'url is incorrect'


@when('I click on sale button')
def step_impl(context):
    context.home_page.click_on_sale_products()


@then('I should be on sale section')
def step_impl(context):
    assert context.home_page.is_sale_products_page(), 'url is incorrect'


@when('I click on search bar box')
def step_impl(context):
    context.home_page.click_on_search_bar()


@when('I input "{product}" product items I want')
def step_impl(context, product):
    context.home_page.enter_product(product)
    time.sleep(2)


@when('I click on search button')
def step_impl(context):
    context.home_page.click_on_search_button()


@then('I should be on page with the searched products')
def step_impl(context):
    time.sleep(3)
    message = context.home_page.is_products_page()
    assert "Search results for: 'pants gym'" in message, 'message not displayed'


@when('I click on the "Diva Gym Tee" product')
def step_impl(context):
    context.home_page.click_on_product()


@when('I select size and colour')
def step_impl(context):
    context.home_page.click_on_size_and_colour()


@when('I click on add to cart button')
def step_impl(context):
    context.home_page.click_on_add_to_cart()


@then('cart counter is incremented by one')
def step_impl(context):
    time.sleep(3)
    assert context.home_page.get_cart_counter() == "1", 'different quantity'


@when('I add an "{product}" product to cart')
def step_impl(context, product):
    context.home_page.add_product_to_cart(product)


@when('I click on basket button')
def step_impl(context):
    context.home_page.click_on_basket_button()
    time.sleep(2)


@when('I click on the remove item icon')
def step_impl(context):
    time.sleep(2)
    context.home_page.remove_item()


@then('cart counter becomes empty')
def step_impl(context):
    time.sleep(3)
    assert context.home_page.get_cart_empty_counter() == "You have no items in your shopping cart.", "different message"
