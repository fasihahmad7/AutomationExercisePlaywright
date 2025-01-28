import pytest
from playwright.sync_api import Playwright, sync_playwright
from typing import Generator

@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    """Fixture for Playwright instance"""
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator:
    """Fixture for browser instance"""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser) -> Generator:
    """Fixture for a new page"""
    context = browser.new_context()  # New browser context for a clean slate
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def setup_with_trace(browser):
    # Create new browser context
    context = browser.new_context()

    # Start tracing with the necessary options
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Create a new page within the context
    page = context.new_page()

    yield page

    # Stop tracing and save it to a file
    context.tracing.stop(path="traces/trace.zip")

    # Close the context
    context.close()
