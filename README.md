# PlaywritePro

UI test automation framework built with **Playwright (Python)** and **pytest**, using the Page Object Model. Tests run against the [Demo Web Shop](https://demowebshop.tricentis.com).

## Features

- Page Object Model with a reusable `BasePage`
- pytest fixtures for Playwright, Browser, BrowserContext and Page (fresh context per test)
- Choose browser (Chromium, Firefox, WebKit) and headless mode from the command line
- Screenshot and Playwright trace saved automatically when a test fails
- Web-first assertions with `expect()` (auto-retry, no fixed sleeps)
- `smoke` and `regression` markers, parametrized tests
- Central configuration (URL, browser, headless)

## Tech stack

Python 3.x, Playwright, pytest

## Project structure

```
PlaywritePro/
├── config/        # config_reader.py and settings
├── pages/         # page objects (base_page, home_page, login_page, register_page)
├── tests/         # test files and base_test.py
├── utils/         # helpers
├── reports/       # failure screenshots and traces (not committed)
├── conftest.py    # fixtures and hooks
├── pytest.ini     # pytest settings and markers
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/Nikhiljen/PlaywritePro.git
cd PlaywritePro
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
playwright install
```

## Run tests

```bash
pytest                                   # all tests
pytest -m smoke                          # smoke tests only
pytest tests/test_home_page.py           # one file
pytest --browser-name=firefox            # choose browser
pytest --headless=false                  # watch the browser
```

## Debug a failure

When a test fails, files are saved in `reports/artifacts/`:

- `<test_name>.png`: screenshot of the page
- `<test_name>.zip`: Playwright trace

Open a trace with:

```bash
playwright show-trace reports/artifacts/<test_name>.zip
```

## Test coverage

Home page, navigation (header and top menu), search, add to cart.

## Roadmap

- [ ] Login and registration tests with JSON test data
- [ ] Parallel runs with pytest-xdist
- [ ] Allure reports
- [ ] GitHub Actions CI

## Author

Nikhil Jengte | [LinkedIn](https://www.linkedin.com/in/nikhiljengte)
