from playwright.sync_api import sync_playwright,expect

def test_locator_chaining():
    with sync_playwright() as playwright:
        browser  = playwright.chromium.launch(headless=False)
        context_page = browser.new_context()
        page = context_page.new_page()

        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        button = page.get_by_text("Add Element")
        for i in range (5):
            button.click()

        delete = page.get_by_text("Delete")

        expect(delete).to_have_count(5)

        print(delete.count())

        delete.first.click()

        expect(delete).to_have_count(4)
        print(delete.count())

        browser.close()