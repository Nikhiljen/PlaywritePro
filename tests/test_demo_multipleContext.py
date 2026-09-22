from playwright.sync_api import sync_playwright

def test_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page_context_1 = browser.new_context()
        page_context_2 = browser.new_context()

        page1 = page_context_1.new_page()
        page2 = page_context_2.new_page()

        page1.goto("https://www.facebook.com/")
        page2.goto("https://www.geeksforgeeks.org/")

        print(page1.title())
        print(page2.title())

        browser.close()