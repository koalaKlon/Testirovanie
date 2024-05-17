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


def filter_movie():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.navigate()
    page.select_genre('boevik')
    page.select_year(['2024', '2023'])
    page.select_collections(['Amazon', 'DC'])
    page.select_sorting('rating')
    time.sleep(10)


def register_user(name='dfsalkj', password='1231afslkd', email='wrewrw', sec_code='asdfa'):
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.register(name, password, email, sec_code)
    time.sleep(10)


def add_movie_to_favorites(username='dfsalkj', password='GSm-XVzy5h8Fa#H', movie_url='https://kinogo.biz/82065-pchelovod.html'):
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.login(username, password)
    page.add_to_favorites(movie_url)
    page.open_favorites()
    time.sleep(10)


def change_password():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.login('dfsalkj', 'GSm-XVzy5h8Fa#H')
    page.password_checker()


def start_watch_movie():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.watch_movie()


def create_comment():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.login('dfsalkj', 'GSm-XVzy5h8Fa#H')
    page.add_comment("Стетхем красава")


def switch_status():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.login('dfsalkj', 'GSm-XVzy5h8Fa#H')
    page.change_movie_status()


def switch_avatar():
    manager = BrowserManager()
    driver = manager.get_driver()
    page = KinogoPage(driver)
    page.login('dfsalkj', 'GSm-XVzy5h8Fa#H')
    page.change_avatar('D:\\Programs\\PyProjects\\Lab9\\bringItOn\\1.png')


if __name__ == '__main__':
    register_user()
    add_movie_to_favorites()
    search_avengers()
    filter_movie()
    change_password()
    create_comment()
    rate_movie()
    switch_avatar()
    switch_status()

