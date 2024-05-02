from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class KinogoPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://kinogo.biz/'
        self.search_input_locator = (By.NAME, 'story')
        self.search_button_locator = (By.CLASS_NAME, 'js-lightsearch-submit')

    def navigate(self):
        self.driver.get(self.url)

    def search(self, query):
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_input_locator))
        search_input.send_keys(query)
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button_locator))
        search_button.click()
        assert "Мстители: финал" in self.driver.page_source, "Search results do not appear as expected"

    def open_movie(self, movie_url):
        self.driver.get(movie_url)
        assert movie_url in self.driver.current_url, "Failed to open the movie page"

    def rate_movie(self, rating):
        rate_button = self.driver.find_element(By.CSS_SELECTOR, f'a.r{rating}-unit[onclick="doRate(\'{rating}\', \'82065\'); return false;"]')
        rate_button.click()


def search_avengers():
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service)
    page = KinogoPage(driver)
    page.navigate()
    page.search('Мстители: финал')
    time.sleep(10)


def rate_movie():
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service)
    page = KinogoPage(driver)
    page.open_movie('https://kinogo.biz/82065-pchelovod.html')
    page.rate_movie(4)
    time.sleep(10)


if __name__ == '__main__':
    #search_avengers()
    rate_movie()