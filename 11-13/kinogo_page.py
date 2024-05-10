from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time


class KinogoPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://kinogo.biz/'
        self.search_input_locator = (By.NAME, 'story')
        self.search_button_locator = (By.CLASS_NAME, 'js-lightsearch-submit')

    def navigate(self):
        logging.info('Navigating to the URL')
        self.driver.get(self.url)

    def search(self, query):
        logging.info('Searching for the query')
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_input_locator))
        search_input.send_keys(query)
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button_locator))
        search_button.click()
        assert "Мстители: финал" in self.driver.page_source, "Search results do not appear as expected"

    def open_movie(self, movie_url):
        logging.info('Opening the movie page')
        self.driver.get(movie_url)
        assert movie_url in self.driver.current_url, "Failed to open the movie page"

    def rate_movie(self, rating):
        logging.info('Rating the movie')
        rate_button = self.driver.find_element(By.CSS_SELECTOR, f'a.r{rating}-unit[onclick="doRate(\'{rating}\', \'82065\'); return false;"]')
        rate_button.click()

    def select_genre(self, genre):
        logging.info(f'Selecting the genre: {genre}')
        genre_link = self.driver.find_element(By.XPATH, f'//a[@href="/{genre}/"]')
        genre_link.click()
        assert genre in self.driver.current_url, f"Failed to select the genre: {genre}"

    def select_year(self, years):
        logging.info(f'Selecting the years: {years}')
        year_button = self.driver.find_element(By.XPATH, '//button[@data-field="y" and contains(@class, "js-xf-filter-toggle xsort__button")]')
        year_button.click()
        for year in years:
            year_option = self.driver.find_element(By.XPATH, f'//button[@title="Год: {year}"]')
            year_option.click()
            assert f'Год: {year}' in self.driver.page_source, f"Failed to select the year: {year}"

    def select_collections(self, collections):
        logging.info(f'Selecting the collections: {collections}')
        collections_button = self.driver.find_element(By.XPATH, '//button[@title="Подборки"]')
        collections_button.click()
        time.sleep(1)
        for collection in collections:
            collection_option = self.driver.find_element(By.XPATH, f'//button[@title="Подборки: {collection}"]')
            collection_option.click()
            assert f'Подборки: {collection}' in self.driver.page_source, f"Failed to select the collection: {collection}"
        collections_button.click()

    def select_sorting(self, sorting):
        logging.info(f'Selecting the sorting mode: {sorting}')
        wait = WebDriverWait(self.driver, 10)
        sorting_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.js-xs-showsort.xsort__button')))
        sorting_button.click()
        sorting_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'button.js-xs-sort[data-value="{sorting}"]')))
        sorting_option.click()
        assert f'data-value="{sorting}"' in self.driver.page_source, f"Failed to select the sorting mode: {sorting}"