from playwright.sync_api import expect


class TestautomatiseringPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.konsultchef_locator = page.get_by_text("konsultchef Test")
        self.varfor_jobba_locator = page.get_by_role("heading", name="Varför ska du jobba hos oss?")

        # Make sure all headings are displayed
        self.verify_page_headings()

    def verify_page_headings(self):
        expect(self.konsultchef_locator).to_be_visible()
        expect(self.varfor_jobba_locator).to_be_visible()

    def click_konsultchef(self, konsultchef_name):
        self.page.get_by_text(konsultchef_name).click()
