from types import TracebackType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Demo_WebScrapping.config.settings import Common_CONFIG


class DriverSeleniumChrome:
    def __init__(self, options: Options = None, service: Service = None, keep_alive: bool = True, teardown=False) -> None:
        options = webdriver.ChromeOptions()

        if Common_CONFIG['START_MAXIMIZED']:
            options.add_argument('--start-maximized')
        
        if Common_CONFIG['DISABLE_EXTENSIONS']:
            options.add_argument('--disable-extensions')
        
        if Common_CONFIG['HEADLESS']:
            options.add_argument('--headless')
        
        self.service = service or Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=options, keep_alive=keep_alive)
        self.teardown = teardown

    def get(self, url):
        self.driver.get(url)

    def find_element_by_text_xpath(self, path, text):
        return self.driver.find_element(By.XPATH, f'//{path}[contains(text(),"{text}")]')
    
    def find_element_by_id_xpath(self, path, element_id):
        return self.driver.find_element(By.XPATH, f'//{path}[@id="{element_id}"]')
    
    def quit(self):
        self.driver.quit()

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.teardown:
            self.quit()
