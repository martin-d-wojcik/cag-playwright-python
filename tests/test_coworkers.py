from pages import homepage, peoplepage


def test_check_out_one_coworker_should_see_headline(chrome_page):
    # Navigate to the homepage
    home_page = homepage.HomePage(chrome_page)
    home_page.close_cookies_popup()
    home_page.heading_visible()
    home_page.click_medarbetare()

    people_page = peoplepage.PeoplePage(chrome_page)
    people_page.verify_something()


