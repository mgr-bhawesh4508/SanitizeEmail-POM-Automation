from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ListValidation(BasePage):
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    REMEMBER_ME = (By.XPATH, "//label[normalize-space()='Remember Me']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Log In']")
    PROFILE_ICON = (By.XPATH, "//button[contains(@class,'rounded-full')]")
    VERIFY_EMAIL = (By.XPATH,"//p[normalize-space()='Verify Email']")
    LIST_VALIDATION = (By.XPATH,"//div[normalize-space()='List Validation']")
    ADD_LIST = (By.XPATH,"//button[contains(@data-slot,'dialog-trigger')]")
    ENTER_EMAILS = (By.XPATH,"//textarea[@id='emails']")
    CHECKBOX = (By.XPATH,"//button[@id='hasChecked']")
    RUN_VALIDATION = (By.XPATH,"//button[normalize-space()='Run Validation']")
    SEARCH_BUTTON = (By.XPATH,"//div[contains(@class,'relative flex items-center')]//*[name()='svg']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def click_remember_me(self):
        self.click_element(self.REMEMBER_ME)

    def click_verify_email(self):
        self.click_element(self.VERIFY_EMAIL)

    def click_list_validation(self):
        self.click_element(self.LIST_VALIDATION)

    def click_add_list(self):
        self.click_element(self.ADD_LIST)

    def enter_emails(self, emails):
        self.enter_text( self.ENTER_EMAILS, emails)

    def click_checkbox(self):
        self.click_element(self.CHECKBOX)

    def click_run_validation(self):
        self.click_element(self.RUN_VALIDATION)