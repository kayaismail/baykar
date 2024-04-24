from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_for_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
