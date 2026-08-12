def test_homepage_title(page):
    page.goto("https://practice.expandtesting.com")
    assert "Practice" in page.title()


def test_login_page_loads(page):
    page.goto("https://practice.expandtesting.com/login")
    page.wait_for_selector("#username")
    assert page.locator("#username").is_visible()


def test_login_with_wrong_credentials(page):
    page.goto("https://practice.expandtesting.com/login")
    page.wait_for_selector("#username")
    page.locator("#username").fill("wronguser")
    page.locator("#password").fill("wrongpassword")
    page.locator("button[type='submit']").click()
    page.wait_for_selector("#flash")
    assert page.locator("#flash").is_visible()


def test_login_with_correct_credentials(page):
    page.goto("https://practice.expandtesting.com/login")
    page.wait_for_selector("#username")
    page.locator("#username").fill("practice")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    page.wait_for_selector("#flash")
    assert page.locator("#flash").is_visible()
