from playwright.sync_api import expect

def alert_accept(dialog):
    print("Alert Message:", dialog.message)
    dialog.accept()

def test_demo_js_alert(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on("dialog", alert_accept)
    page.get_by_role("button", name="Click for JS Alert").click()

    result = page.locator("#result")
    expect(result).to_be_visible()
    print("Result:", result.inner_text())

def  test_demo_js_confirm(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", alert_accept)
    page.get_by_role("button",name="Click for JS Confirm").click()

    result = page.locator("#result")
    expect(result).to_be_visible()
    print("Result:", result.inner_text())

def  test_demo_js_dismiss(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button",name="Click for JS Confirm").click()

    result = page.locator("#result")
    expect(result).to_be_visible()
    print("Result:", result.inner_text())


def  test_demo_js_prompt(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.accept("Nikhil"))
    page.get_by_role("button",name="Click for JS Prompt").click()

    result = page.locator("#result")
    expect(result).to_be_visible()
    print("Result:", result.inner_text())
