from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def search_avengers():
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service)

    driver.get('https://kinogo.biz/')

    search_input = driver.find_element(By.NAME, 'story')

    search_input.send_keys('Мстители: финал')

    search_button = driver.find_element(By.CLASS_NAME, 'js-lightsearch-submit')
    search_button.click()

    time.sleep(10)


if __name__ == '__main__':
    search_avengers()