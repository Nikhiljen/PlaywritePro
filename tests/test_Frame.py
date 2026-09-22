from playwright.sync_api import expect


def test_frame(page):
    page.goto("https://the-internet.herokuapp.com/iframe")
    frame = page.frame_locator("mce_0_ifr")
    ele = frame.get_by_text("Your content goes here.")
    ele.clear()
    ele.fill("Learning Playwright with Python")

    expect(ele).to_have_text("Learning Playwright with Python")