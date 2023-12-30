from playwright.sync_api import sync_playwright


def set_up_browser(browser_name):
    with sync_playwright() as playwright:
        match browser_name:
            case 'chrome':
                browser = playwright.chromium.launch(headless=False)
            case 'firefox':
                browser = playwright.firefox.launch(headless=False)
            case 'webkit':
                browser = playwright.webkit.launch(headless=False)
        page = browser.new_page()
        return page
