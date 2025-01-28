import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function")
def setup_teardown(page: Page):
    page.goto('http://automationexercise.com')
    yield page

def test_contact_us_form_submission(setup_teardown):
    page = setup_teardown
    
    # 1. Verify home page
    expect(page).to_have_title("Automation Exercise")

    # 2. Navigate to Contact Us
    with page.expect_navigation():
        page.get_by_role("link", name="Contact us").click()

    assert page.locator("text=Get In Touch").is_visible()

    # 3. Fill form using reliable selectors
    form_data = {
        "name": "Test User",
        "email": "test@example.com",
        "subject": "Test Subject",
        "message": "Test message"
    }

    page.locator("input[name='name']").fill(form_data["name"])
    page.locator("input[name='email']").fill(form_data["email"])
    page.locator("input[name='subject']").fill(form_data["subject"])
    page.locator("textarea[name='message']").fill(form_data["message"])

    # 4. Submit form with navigation wait
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("input[name='submit']").click()

    expect(page).to_have_title("Automation Exercise - Contact Us")
    page.click("a[class='btn btn-success'] span")
    assert page.title() == "Automation Exercise"
    print("Test passed: Filled contact us form")