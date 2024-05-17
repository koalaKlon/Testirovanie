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

    def navigate_to_registration(self):
        logging.info('Navigating to the registration page')
        self.driver.get('https://kinogo.biz/index.php?do=register')

    def accept_terms(self):
        logging.info('Accepting the terms')
        accept_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.bbcodes[value="Принимаю"]')))
        accept_button.click()

    def enter_registration_details(self, name, password, email, sec_code):
        logging.info('Entering the registration details')
        name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'name')))
        name_input.send_keys(name)

        password1_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'password1')))
        password1_input.send_keys(password)

        password2_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'password2')))
        password2_input.send_keys(password)

        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        email_input.send_keys(email)

        sec_code_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'sec_code')))
        sec_code_input.send_keys(sec_code)

    def submit_registration(self):
        logging.info('Submitting the registration form')
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn[name="submit"]')))
        submit_button.click()

    def register(self, name, password, email, sec_code):
        self.navigate_to_registration()
        self.accept_terms()
        self.enter_registration_details(name, password, email, sec_code)
        self.submit_registration()

    def login(self, username, password):
        logging.info('Logging in')
        self.driver.get('https://kinogo.biz/index.php?do=login')
        time.sleep(3)

        logging.info('Clicking on the login link')
        login_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[onclick="change(\'test\')"]')))
        login_link.click()

        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'login_name')))
        username_input.send_keys(username)
        time.sleep(3)
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'login_password')))
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.fbutton2[title="Войти"]')))
        login_button.click()

    def add_to_favorites(self, movie_url):
        logging.info('Adding movie to favorites')
        time.sleep(2)
        self.driver.get(movie_url)
        self.driver.execute_script("document.querySelector('a[title=\"Закладки\"] span').click();")

    def open_favorites(self):
        logging.info('Opening favorites')
        self.driver.get('https://kinogo.biz/favorites/')

    def password_checker(self):
        logging.info('Checking password')
        self.driver.get('https://kinogo.biz/user/dfsalkj/')
        logging.info('Finding and clicking on the "edit profile" link')
        edit_profile_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'редактировать профиль')))
        time.sleep(2)
        edit_profile_link.click()
        time.sleep(2)
        self.driver.find_element(By.NAME, 'altpass').send_keys('GSm-XVzy5h8Fa#H')
        self.driver.find_element(By.NAME, 'password1').send_keys('sdfas12314')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(5)

    def watch_movie(self):
        logging.info('Watching movie')
        self.driver.get('https://kinogo.biz/82065-pchelovod.html')
        time.sleep(5)
        play_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.play-button')))
        play_button.click()

    def add_comment(self, comment):
        logging.info('Adding comment')
        self.driver.get('https://kinogo.biz/82065-pchelovod.html')

        add_comment_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//span[contains(@onclick, "commentForm") and contains(@onclick, "toggle")]')))
        add_comment_button.click()

        comment_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'comments')))
        comment_input.send_keys(comment)

        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.fbutton[title="Добавить комментарий"]')))
        submit_button.click()
        time.sleep(10)

    def change_movie_status(self):
        logging.info('Changing movie status')
        self.driver.get('https://kinogo.biz/82065-pchelovod.html')
        watched_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.usermark__item[data-folder="done"]')))
        watched_button.click()
        time.sleep(10)

    def change_avatar(self, image_path):
        logging.info('Changing avatar')
        self.driver.get('https://kinogo.biz/user/dfsalkj/')
        time.sleep(3)
        edit_profile_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "javascript:ShowOrHide(\'options\')")]')))
        edit_profile_button.click()
        time.sleep(3)
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'image')))
        file_input.send_keys(image_path)
        time.sleep(3)
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.fbutton[value="Сохранить"]')))
        save_button.click()
        time.sleep(10)