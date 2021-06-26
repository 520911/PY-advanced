import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class TestYaAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://passport.yandex.ru/auth/')
        self.assertIn('Авторизация', self.driver.title)

    def test_login_in_ya(self):
        elem = self.driver.find_element_by_name('login')
        sleep(2)
        elem.send_keys('zmremont')
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        sleep(2)
        elem = self.driver.find_element_by_name('passwd')
        elem.send_keys('Denis520911$$')
        elem.send_keys(Keys.RETURN)
        sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

