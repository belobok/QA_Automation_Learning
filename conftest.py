import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Always use Safari on macOS to avoid Chrome/driver mismatch
    d = webdriver.Safari()
    yield d
    d.quit()
