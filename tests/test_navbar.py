import unittest
from selenium import webdriver
from base.base_functions import Base
from pages.home_page import HomePage


class TestNavbar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_page = Base(self.driver)
        self.home_page = HomePage(self.driver)

    def test_navbar_elements(self):
        self.base_page.go_to_url("https://www.kariyer.baykartech.com/")
        navbar_elements = self.home_page.get_navbar_elements()
        num_elements = len(navbar_elements)

        for i in range(num_elements):
            self.home_page.click_navbar_element(i)
            self.base_page.wait_for_title("Baykar Technologies")
            self.assertIn("Baykar Technologies", self.driver.title)
            self.base_page.go_to_url("https://www.kariyer.baykartech.com/")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
