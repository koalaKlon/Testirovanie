from browser_manager import BrowserManager
from kinogo_page import KinogoPage
import time


def search_avengers():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.navigate()
    page.search('Мстители: финал')
    time.sleep(10)


def rate_movie():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.open_movie('https://kinogo.biz/82065-pchelovod.html')
    page.rate_movie(4)
    time.sleep(10)


def run_test():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.navigate()
    page.select_genre('boevik')
    page.select_year(['2024', '2023'])
    page.select_collections(['Amazon', 'DC'])
    page.select_sorting('rating')
    time.sleep(10)


if __name__ == '__main__':
    run_test()
    search_avengers()
    rate_movie()
