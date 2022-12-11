from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class MySelenium(): 

    def __init__(self, url, size='400,1080'):
        self.url = url
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')  
        chrome_options.add_argument(f'--window-size={size}') 
        chrome_options.add_argument("--disable-notifications")
        # chrome_options.add_argument("--remote-debugging-port=9222")       
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.implicitly_wait(10)
   
    def photo(self, path_photo):
        print(f"Photo: {path_photo}")
        self.browser.save_screenshot(path_photo)

    def visit(self):
        print(f"Visit: {self.url}")
        self.browser.get(self.url)

    def input(self,attr_type,attr_val,value):
        self.browser.find_element(attr_type,attr_val).send_keys(value)

    def click(self,attr_type,attr_val):
        self.browser.find_element(attr_type,attr_val).click()