import pytest
from playwright.sync_api import sync_playwright
from pages import carreerpage


@pytest.fixture(name='chrome_page', scope='module', autouse=True)
def set_up_chrome():
    with sync_playwright() as playwright:
        # Set headless to True when running tests in container
        browser = playwright.chromium.launch(headless=True)
        global page
        page = browser.new_page()
        yield page

@pytest.fixture()
def page(browser):
    page = browser.new_context().new_page()
    yield page

@pytest.fixture
def home_page(browser):
    print('carreer_page fixture')
    page = browser.new_context().new_page()
    carreer_page = carreerpage.CarreerPage(browser)
    yield carreer_page
