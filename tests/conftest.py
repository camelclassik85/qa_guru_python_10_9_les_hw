import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_open():
    browser.config.window_width = 1080
    browser.config.window_height = 720
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()
