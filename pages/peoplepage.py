from playwright.sync_api import expect


class PeoplePage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.kontakta_oss_locator = page.get_by_role("heading", name="Kontakta oss")
        self.testautomatisering_link_locator = page.get_by_role("heading", name="Test & Testautomatisering").get_by_role("link")

    def kontakta_oss_visible(self):
        expect(self.kontakta_oss_locator).to_be_visible()

    def click_testautomatisering(self):
        self.testautomatisering_link_locator.click()