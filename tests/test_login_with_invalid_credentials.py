def test_login_with_invalid_credentials(page):
    print("Running Test case 4 - Verify login with invalid credentials")
    page.goto("https://automationexercise.com/")
    assert page.title() == "Automation Exercise"
    page.click("a[href='/login']")
    login_header = page.locator("text=Login to your account")
    assert login_header.is_visible()
    page.fill("input[data-qa='login-email']", "testusery@example.com")
    page.fill("input[placeholder='Password']", "passwor")
    page.click("button[data-qa='login-button']")
    assert page.locator("text=Your email or password is incorrect!").is_visible()
    print("Test Passed: Error message displayed for invalid login \n")