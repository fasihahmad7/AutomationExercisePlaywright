import time
def logout_user(page):
    print("Running Test case 4 - Logout user")
    page.goto("https://automationexercise.com/")
    assert page.title() == "Automation Exercise"
    page.click("a[href='/login']")
    login_header = page.locator("text=Login to your account")
    assert login_header.is_visible()
    page.fill("input[data-qa='login-email']", "testuseryf6xw9@example.com")
    page.fill("input[placeholder='Password']", "password123")
    page.click("button[data-qa='login-button']")
    assert page.locator("text=Logged in as Test User").is_visible()
    page.click("a[href='/logout']")
    login_header = page.locator("text=Login to your account")
    assert login_header.is_visible()