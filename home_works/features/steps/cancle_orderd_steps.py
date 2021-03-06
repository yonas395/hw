from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
SEARCH_BTN = (By.XPATH, "//div[@class='a-box a-spacing-extra-large answer-box answer-box-t1']" )
BB_SEARCH = (By.ID, 'twotabsearchtextbox')
SUBMIT = (By.ID, 'nav-search-submit-button')
F_ITEM = (By.XPATH, "//div[@data-component-type='s-impression-counter']//div[@class='a-price-whole']" )
bst_sell = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a")



@given('open {amazon} page')
def open_amazon(context, amazon):
    context.driver.get("https://www.amazon.com/")
    context.driver.get("https://www.amazon.com/gp/bestsellers/")
    sleep(1)



@when('search for {search_word}')
def open_customer_service(context, search_word):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")
    sleep(1)




@then('search for {search_word}')
def open_canceled_items(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys('cancel order', Keys.ENTER)
    context.driver.find_element(*BB_SEARCH).send_keys('basketball', Keys.ENTER)
    sleep(2)



@then('verify the {canceled_item_or_order} page comes')
def verify_canceled_page(context, canceled_item_or_order):
    expected_result = 'Cancel Items or Orders You can cancel items or orders that have not shipped by visiting the Order ' \
                      'section in Your Account '
    actual_result = context.driver.find_element(*SEARCH_BTN).text

    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'


@then('verify there are {expected_amount} links')
def verify_there_are_links(context, expected_amount):
    header_links = context.driver.find_elements(*bst_sell)
    assert len(header_links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(header_links)}'















