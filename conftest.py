import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()