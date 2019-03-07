from firefox_browser import FirefoxBrowser
from webhelper import WebHelper
from selenium import webdriver

class Main:
    def __init__(self):
        self.tier=1
        self.ff = FirefoxBrowser(tier=self.tier,desktop=True)
        self.driver = self.ff.driver
        self.webhelper=WebHelper(self.driver)
        self.login()

    def login(self):
        url='https://engine-cchaos-staging.herokuapp.com/admin/products'
        self.webhelper.go_to(url)

        self.webhelper.send_keys(
            element=self.webhelper.locate_element(
                m=self.driver.find_element_by_xpath,
                n='//*[@id="spree_user_email"]'
            ),
            string='chadwick+admin@enginecommerce.com')

        self.webhelper.send_keys(
            element=self.webhelper.locate_element(
                m=self.driver.find_element_by_xpath,
                n='//*[@id="spree_user_password"]'
            ),
            string='Test123')

        self.webhelper.locate_element(m=self.driver.find_element_by_xpath,
            n='/html/body/main/div/form/p[3]/input'
            ).click()

        if current_url == 'https://engine-cchaos-staging.herokuapp.com/admin/products':
            return True
        return False

main=Main()
