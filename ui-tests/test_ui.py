def test_homepage_title(page):
    page.goto("https://practicesoftwaretesting.com")
    assert "Practice Software Testing" in page.title()


def test_search_returns_results(page):
    page.goto("https://practicesoftwaretesting.com")
    page.locator("input[placeholder='Search']").fill("pliers")
    page.keyboard.press("Enter")
    page.wait_for_load_state("domcontentloaded")
    assert page.locator(".card").count() > 0


def test_login_page_loads(page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.wait_for_selector("input[formcontrolname='email']")
    assert page.locator("input[formcontrolname='email']").is_visible()


def test_homepage_shows_products(page):
    page.goto("https://practicesoftwaretesting.com")
    page.wait_for_selector(".card")
    assert page.locator(".card").count() > 0
