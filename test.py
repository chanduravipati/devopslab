from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test cases
test_cases = [
    {
        "username": "User NoEmail",
        "email": "",
        "password": "password123"
    },
    {
        "username": "ShortPasswordUser",
        "email": "shortpass@example.com",
        "password": "123"
    },
    {
        "username": "ValidUser",
        "email": "validuser@example.com",
        "password": "validpassword123"
    }
]
# Set up ChromeDriver
driver = webdriver.Chrome()
try:
    # Load the local HTML file
    driver.get("http://127.0.0.1:5000")  # Replace with the correct path

    for test in test_cases:
        # Refresh the page for each test case
        driver.refresh()
        time.sleep(1)

        # Fill in the form fields
        driver.find_element(By.ID, "username").send_keys(test["username"])
        driver.find_element(By.ID, "email").send_keys(test["email"])
        driver.find_element(By.ID, "password").send_keys(test["password"])

        # Click the register button
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # Capture and print alert messages
        try:
            alert = driver.switch_to.alert
            print(f"Test Case: {test['username']} - Alert: {alert.text}")
            alert.accept()
        except:
            print(f"Test Case: {test['username']} - No Alert Triggered")

        time.sleep(2)

finally:
    # Close the browser
    driver.quit()
