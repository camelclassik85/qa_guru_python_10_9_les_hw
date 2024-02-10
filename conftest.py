import pytest
from selene import browser

BASE_URL = 'https://github.com'


@pytest.fixture(autouse=True)
def browser_open():
    browser.config.window_width = 1080
    browser.config.window_height = 720
    browser.config.base_url = BASE_URL

    yield

    browser.quit()
