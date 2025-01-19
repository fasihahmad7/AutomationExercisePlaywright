import time
def test_contact_us(page):
    print("Running Test case 6 - Contact us form")
    page.goto("https://automationexercise.com/")
    assert page.title() == "Automation Exercise"
    page.click("a[href='/contact_us']")
    assert page.locator("text=Contact Us").is_visible()
    page.fill("input[placeholder='Name']", "John Doe")
    page.fill("input[placeholder='Email']", "johndoe@example.com")
    page.fill("input[placeholder='Subject']", "Test Subject")
    page.fill("#message", "This is a test message.")
    page.click("input[name='submit']")
    page.on("dialog", lambda dialog: dialog.accept())
    time.sleep(5)
    assert page.locator("text=Success! Your details have been submitted successfully.").is_visible()
    page.click("a[class='btn btn-success'] span")
    assert page.title() == "Automation Exercise"
    print("Test passed: Filled contact us form")
