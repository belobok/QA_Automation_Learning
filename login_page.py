from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")

    # On success, the site redirects to /logged-in-successfully/
    SUCCESS_URL_PART = "logged-in-successfully"
    SUCCESS_HEADING = (By.TAG_NAME, "h1")  # heading: "Logged In Successfully" on success
    SUCCESS_TEXT = (By.XPATH, "//*[contains(.,'successfully logged in') or contains(.,'Logged In Successfully')]")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()

    def wait_for_success(self):
        # Wait for either the URL to contain the success path
        # OR a success heading/text to show up.
        try:
            self.wait.until(EC.url_contains(self.SUCCESS_URL_PART))
        except Exception:
            # Fallback: wait for heading/text if URL check didn't trigger yet
            self.wait.until(
                EC.any_of(
                    EC.presence_of_element_located(self.SUCCESS_HEADING),
                    EC.presence_of_element_located(self.SUCCESS_TEXT),
                )
            )

    def success_text(self) -> str:
        # Try heading first; if not present, try paragraph/text
        try:
            h1 = self.driver.find_element(*self.SUCCESS_HEADING).text
            if h1:
                return h1
        except Exception:
            pass
        try:
            return self.driver.find_element(*self.SUCCESS_TEXT).text
        except Exception:
            return ""

