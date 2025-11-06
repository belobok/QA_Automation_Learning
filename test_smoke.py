def test_safari_smoke(driver):
    driver.get("https://example.com")
    assert "Example" in driver.title
