from pages.login_page import LoginPage

def test_success_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("student", "Password123")
    page.wait_for_success()
    assert "success" in page.success_text().lower()

