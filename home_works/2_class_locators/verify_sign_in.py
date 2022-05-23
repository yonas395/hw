from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/JetBrains/chromedriver.exe")
driver.get("https://www.amazon.com/")

var = driver.find_element(By.XPATH, "//span[text()='& Orders']").click()

    expected_result = 'sign in page must come'
    actual_result = context.driver.get(f"https://www.amazon.com/ap/signin?")

    assert expected_result == actual_result,  f'Error! Actual text {actual_result} does not match expected{expected_result}'




