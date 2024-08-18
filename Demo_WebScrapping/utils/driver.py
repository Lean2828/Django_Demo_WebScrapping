from types import TracebackType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Demo_WebScrapping.config.settings import Common_CONFIG
import os


class DriverSeleniumChrome:
    def __init__(self, options: Options = None, service: Service = None, keep_alive: bool = True, teardown=False) -> None:
        options = webdriver.ChromeOptions()

        if Common_CONFIG['START_MAXIMIZED']:
            options.add_argument('--start-maximized')
        
        if Common_CONFIG['DISABLE_EXTENSIONS']:
            options.add_argument('--disable-extensions')
        
        if Common_CONFIG['HEADLESS']:
            options.add_argument('--headless')
            
        if Common_CONFIG['DISABLE_GPU']:
            options.add_argument('--disable-gpu')            
            
        if Common_CONFIG['NO_SANDBOX']:
            options.add_argument('--no-sandbox')                        
            
        if Common_CONFIG['DISABLE_EXTENSIONS']:
            options.add_argument('--disable-extensions') 
            
        options.add_argument('--disable-dev-shm-usage')
        
        self.service = service
        
        # self.service = service or Service(ChromeDriverManager().install())
        if not self.service:
            # Determinar el executable_path basado en la variable de entorno CHROMEDRIVER_PATH o usar ChromeDriverManager
            executable_path = os.getenv('CHROMEDRIVER_PATH', None)
            if executable_path:
                self.service = Service(executable_path=executable_path)
            else:
                self.service = Service(ChromeDriverManager().install())        
        
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
