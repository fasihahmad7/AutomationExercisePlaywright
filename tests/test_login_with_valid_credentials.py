def test_login_with_valid_credentials(page):
    print("Running Test case 2 - Verify login with valid credentials")
    page.goto("https://automationexercise.com/")
    assert page.title() == "Automation Exercise"
    page.click("a[href='/login']")
    login_header = page.locator("text=Login to your account")
    assert login_header.is_visible()
    page.fill("input[data-qa='login-email']", "testuseryf6xw9@example.com")
    page.fill("input[placeholder='Password']", "password123")
    page.click("button[data-qa='login-button']")
    assert page.locator("text=Logged in as Test User").is_visible()
    print("Test Passed: Login Successfull. \n")
