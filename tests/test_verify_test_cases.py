def verify_test_cases(page):
    print("Running Test 7 - Verify Test cases ")
    page.goto("https://automationexercise.com/")
    assert page.title() == "Automation Exercise"
    page.click("div[class='item active'] a[class='test_cases_list'] button[type='button']")
    assert page.locator("text=Test Cases").is_visible()
    print("Test passed: Naigated to test cases")