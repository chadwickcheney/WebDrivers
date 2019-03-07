class WebHelper:
    def __init__(self, driver):
        self.driver=driver

    def go_to(self,url):
        self.driver.get(url)

    def locate_element(self,m,n):
        return m(n)

    def send_keys(self, element, string):
        element.send_keys(string)
        return True
