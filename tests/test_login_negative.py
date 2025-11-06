from pages.login_page import LoginPage

def test_login_invalid_password_shows_error(driver):
    page = LoginPage(driver)
    page.open()
    page.login("student", "WrongPassword")
    # Simple proof the error is shown on page
    assert "Your password is invalid!" in driver.page_source
