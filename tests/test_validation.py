from utils.test_runner import create_driver
from pages.validation_page import ListValidation
from data.test_data import EMAILS
import pytest
import time
from utils.assertions import assert_true
import allure

class TestListValidation:
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://app.sanitizeemail.com/")

        self.validation_page = ListValidation(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("data", EMAILS)
    @allure.title("Test of list validation using emails list:")
    def test_list_validation(self, data):
        with allure.step("Login"):
            self.validation_page.enter_email(data["email"])
            self.validation_page.enter_password(data["password"])
            self.validation_page.click_remember_me()
            self.validation_page.click_login_button()
            self.validation_page.wait_for_element_visible(self.validation_page.PROFILE_ICON)

        with allure.step("Navigate to list validation"):
            self.validation_page.click_verify_email()
            self.validation_page.click_list_validation()
            self.validation_page.wait_for_element_visible(self.validation_page.ADD_LIST)

        with allure.step("Click add list"):
            self.validation_page.click_add_list()

        with allure.step("Enter Emails and Run Validation"):
            emails_text = "\n".join(data["emails_list"])

            self.validation_page.enter_text(self.validation_page.ENTER_EMAILS, emails_text)
            self.validation_page.click_element(self.validation_page.CHECKBOX)
            self.validation_page.click_element(self.validation_page.RUN_VALIDATION)
            time.sleep(30)
            # self.validation_page.wait_for_element_visible(self.validation_page.SEARCH_BUTTON)

        with allure.step("Assertion"):
            assert_true(
                self.validation_page.is_element_visible(self.validation_page.SEARCH_BUTTON),
                "Validation failed as the Email validation heading is not visible",
                "Validation",
                self.validation_page
            )