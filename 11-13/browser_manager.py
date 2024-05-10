from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserManager:
    def __init__(self):
        self.options = Options()
        self.webdriver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.webdriver_service, options=self.options)

    def get_driver(self):
        return self.driver
