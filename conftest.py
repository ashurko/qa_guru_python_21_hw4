import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()