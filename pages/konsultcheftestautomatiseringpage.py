from playwright.sync_api import expect


class KonsultchefTestautomatisering:
    def __init__(self, page):
        self.page = page

        # locators
        self.konsultchef_email_locator = page.get_by_title("E-post")
        # self.konsultchef_email_adress_locator = page.get_by_role("link", name="david.caro@cag.se", exact=True)
        self.konsultchef_telephone_locator = page.get_by_title("Telefon")
        # self.konsultchef_phonenumber_locator = page.get_by_role("link", name="0709343340", exact=True)

    def verify_email_and_phone_number(self, email, phnoenumber):
        self.konsultchef_email_locator.click()
        expect(self.page.get_by_role("link", name=email, exact=True)).to_be_visible()

        self.konsultchef_telephone_locator.click()
        expect(self.page.get_by_role("link", name=phnoenumber, exact=True)).to_be_visible()
