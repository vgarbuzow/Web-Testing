from selenium import webdriver
import pytest


@pytest.fixture()
def get_chrome_driver():
    with webdriver.Chrome() as driver:
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(5)
        yield driver



