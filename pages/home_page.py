from selenium.webdriver.common.by import By
from base.base_functions import Base


class HomePage(Base):
    NAVBAR_ELEMENTS = (By.CSS_SELECTOR, ".navbar-nav li a")

    def get_navbar_elements(self):
        return self.driver.find_elements(*self.NAVBAR_ELEMENTS)

    def click_navbar_element(self, element_index):
        navbar_elements = self.get_navbar_elements()
        navbar_elements[element_index].click()
