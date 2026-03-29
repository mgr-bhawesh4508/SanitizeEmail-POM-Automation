from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time
import allure

class BasePage():
    def __init__(self, driver):
        # Store the driver instance
        self.driver = driver
        # Wait up to 10 seconds for elements
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        # Wait until element is present in DOM
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        # Wait until element is clickable
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        try:
            element = self.find_clickable_element(locator)
            element.click()
        except Exception as e:
            element_name = locator.split("/"[-1]).replace("'", "").replace('"', '')
            self.take_screenshot(f"Click_failure_{element_name}")
            raise e

    def enter_text(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            element_name = locator.split("/"[-1]).replace("'", "").replace('"', '')
            self.take_screenshot(f"Send_keys_failure_{element_name}")
            raise e

    def is_element_present(self, locator):
            try:
                self.find_element(locator)
                return True
            except TimeoutException:
                return False

    def is_element_visible(self, locator):
            try:
                self.find_element(locator)
                return True
            except TimeoutException:
                return False

    def get_element_text(self, locator):
            element = self.find_element(locator)
            return element.text

    def take_screenshot(self, name):
        # Create Screenshots folder if not present
        if not os.path.exists("Screenshots"):
            os.makedirs("Screenshots")

        timestamp = int(time.time())
        file_path = f"Screenshots/{name}_{timestamp}.png"

        # Take screenshot
        self.driver.save_screenshot(file_path)

        # Attach screenshot to Allure report
        allure.attach.file(
            file_path,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

