def test_window(page):
    page.goto("https://the-internet.herokuapp.com/windows")
    content = page.locator("#content")
    with page.expect_popup() as new_window:
        content.get_by_role("link",name="Click Here").click()
    #     content.get_by_role("link")

    new_page = new_window.value
    print(new_page.title())
    new_page.close()
    print(page.title())
