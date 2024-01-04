from playwright.sync_api import expect


class CarreerPage:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://careers.contactor.cag.se/")

        # Locators
        self.accept_cookies_button_locator = page.get_by_role("button", name="Acceptera alla cookies")
        heading_name = 'CAG Contactor - Konsulter som trivs är vår främsta framgångsfaktor'
        self.heading_locator = page.get_by_role("heading", name=heading_name)
        self.medarbetare_link_locator = page.get_by_role("link", name="Medarbetare", exact=True)
        self.connect_link_locator = page.get_by_role("link", name="Connect", exact=True)

    def close_cookies_popup(self):
        self.accept_cookies_button_locator.click()

    def heading_visible(self):
        expect(self.heading_locator).to_be_visible()

    def click_medarbetare(self):
        self.medarbetare_link_locator.click()

    def click_connect(self):
        self.connect_link_locator.click()