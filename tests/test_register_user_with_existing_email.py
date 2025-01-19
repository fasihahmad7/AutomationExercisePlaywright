def test_register_user_with_existing_email(page):
    print("Running Test case 5 - Register User with existing email")
    page.goto("https://automationexercise.com/")
    assert page.title() == "Automation Exercise"
    page.click("a[href='/login']")
    signup_header = page.locator("text=New User Signup!")
    assert signup_header.is_visible()
    page.fill("input[placeholder='Name']", "S25")
    page.fill("input[data-qa='signup-email']", "testuseryf6xw9@example.com")
    page.click("button[data-qa='signup-button']")
    assert page.locator("text=Email Address already exist!").is_visible()
    print("Test passed: User cannot register using existing email")
