from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_driver():
    """Create and return a Chrome WebDriver instance"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # # Add Incognito mode
    # chrome_options.add_argument("--incognito")

    # Update this path to your actual chromedriver location
    service = Service(r"C:\Users\97155\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

    # Initialize the driver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver