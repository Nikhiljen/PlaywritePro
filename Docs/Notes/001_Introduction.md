What Is Playwright?
Playwright is a open source automation framework.
it supports
Chromium
Firefox
Safari engine

With one open API, Automate all three browser

Advantage over selenium?
Auto waiting is built in in pw where in selenium manuale set up wait eg. explicit wait
Built in network interception
Sep. driver management is not required
faster and simpler setup

Diff Between Sync and async in pw?
In Sync Each line is wait to finish the previous one to finish
Task 1 ---> Wait ---> Task 2---> Wait ---> Task3

In Async allows program to wait on other tasks while waiting for operation to finish
Task 1 ---> Waiting ---> Do Another Task ---> Task Complete ---> return To Task 1

browser.close() ---> used to free resources

What is Browser Context ?
A Browser Context is an isolated browser session within a browser instance.

Think of it as opening a new Incognito/Private window.

Each context has its own:

Cookies
Local Storage
Session Storage
Cache
Permissions

Contexts do not share data with each other.

       Playwright
            │
      Browser (Chrome)
           │
    ├──────────────┐
    │              │
 Context 1     Context 2
 (User A)      (User B)
  │              │
  Page          Page
 
Even though both contexts use the same Chrome browser process, they are completely isolated

Creating a Browser Context

context = browser.new_context()
page = context.new_page()

Multiple Contexts Example
admin_context = browser.new_context()
customer_context = browser.new_context()

admin_page = admin_context.new_page()
customer_page = customer_context.new_page()

admin_page.goto("https://example.com")
customer_page.goto("https://example.com")

Why Not Just Open Two Tabs?
Used a Same resources same session
If you log in on Page 1, Page 2 is also logged in because they share the same cookies and session.

Browser
   │
Context
   ├── Page 1
   ├── Page 2
   └── Page 3

All three pages share the same login session because they're in the same context.

Interview Questions
Q1. What is a Browser Context?

Answer:
A Browser Context is an isolated browser session within a browser instance. It has its own cookies, local storage, session storage, and permissions, allowing multiple independent users to be simulated in the same browser.

Q2. Why use Browser Context instead of multiple browsers?

Answer:
Creating multiple browser contexts is much faster and uses fewer system resources than launching multiple browser instances, while still providing complete session isolation.

Q3. Can one Browser Context have multiple pages?

Answer:
Yes. A single browser context can contain multiple pages (tabs), and those pages share the same session data such as cookies and local storage.

If Browser Context is the heart of Playwright, Locators are its soul.

A locator is a way to identify an element on a web page.

In Selenium we wright ---> driver.findElements(locator)
In PlayWright ---> page.locator()

order of preference ---> get_by_role → get_by_text() → get_by_label() → get_by_placeholder() → css selector(#className/.id) → XPath

Why are Playwright locators more reliable than Selenium's findElement()?
Playwright locators are more reliable because they are lazy and include automatic waiting.
In Selenium:

findElement() immediately searches for the element.
If the element is not present, Selenium throws NoSuchElementException.
We usually need Explicit Waits or Fluent Waits.

Playwright automatically waits until the button:

exists
is visible
is enabled
is stable (not moving)

Then it clicks.

What is Auto-Waiting?
Auto-waiting allows Playwright to wait automatically for elements to become actionable before interacting with them.

Why did you use: get_by_role instead of page.locator
It is based on accessibility roles, making tests more reliable and readable.
It is less likely to break if the page layout changes.
XPath is more fragile because it depends on the HTML structure.

Actionability Checks
Before click(), Playwright automatically performs these checks:
Check	Why?
Attached	Element exists
Visible	User can see it
Stable	Not moving
Enabled	Can be interacted with
Receives Events	Not blocked by another element

This is why Playwright tests are generally more stable than Selenium tests.

1. What is Auto-Waiting?
Answer: Auto-waiting is Playwright's feature that automatically waits for elements to become ready before interacting with them, reducing flaky tests and the need for manual waits.

2. What are Actionability Checks?
Answer: Before performing actions like click(), Playwright verifies that the element is attached, visible, stable, enabled, and able to receive events.

3. Why is Playwright more stable than Selenium?
Answer: One major reason is that Playwright includes built-in auto-waiting and actionability checks, so tests don't rely as heavily on manual waits.

4. Why should you avoid time.sleep()?
Answer: It introduces fixed delays, making tests slower and more brittle because it waits even when the application is already ready.

Click Edit for a Specific Row
Suppose:
John      Edit
David     Edit
Mike      Edit

row = page.locator("tr").filter(has_text="David")
row.get_by_role("button", name="Edit").click()
This is a common interview question.

Feature	                               Purpose
has	                        Filter elements that contain another element
has_text	                Filter elements by text content
has_not	                    Filter elements that do not contain another element
following-sibling (XPath)	Navigate to the next sibling element

Q1. What is Locator Chaining?
Answer: Locator chaining allows you to locate an element within another locator, making selectors more readable and maintainable.

Q2. What is filter() used for?
Answer: filter() narrows down a set of matching locators based on text (has_text) or the presence of another locator (has).

Q3. What is the difference between first, last, and nth()?
first → first matching element
last → last matching element
nth(index) → element at a specific zero-based index

Q4. Why should you avoid using nth() when possible?
Answer: If the page order changes, the index changes too, making tests fragile. 
Prefer unique locators based on roles, labels, or text.