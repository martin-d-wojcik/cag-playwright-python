from pages import homepage, peoplepage, testautomatiseringpage, konsultcheftestautomatiseringpage


# Call the chrome_page fixture to set up a chrome page
def test_check_out_one_coworker_should_see_email_and_phonenumber(chrome_page):
    # Navigate to the homepage
    home_page = homepage.HomePage(chrome_page)
    home_page.close_cookies_popup()
    home_page.heading_visible()
    home_page.click_medarbetare()

    # Click the Test & Testautomatisering link
    people_page = peoplepage.PeoplePage(chrome_page)
    people_page.kontakta_oss_visible()
    people_page.click_testautomatisering()

    # Click konsultchef and verify that guy
    testautomatisering_page = testautomatiseringpage.TestautomatiseringPage(chrome_page)
    testautomatisering_page.click_konsultchef()

    # Assert email adress and phonenumber
    konsultchef_testautomatisering_page = konsultcheftestautomatiseringpage.KonsultchefTestautomatisering(chrome_page)
    konsultchef_testautomatisering_page.verify_email_and_phone_number()


