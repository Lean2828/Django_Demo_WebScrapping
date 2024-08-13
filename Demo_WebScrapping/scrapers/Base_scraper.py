from Demo_WebScrapping.utils.driver import  DriverSeleniumChrome

class BaseScraper:
    def __init__(self, config):
        self.config = config
        self.driver = DriverSeleniumChrome()

    def scrape(self):
        raise NotImplementedError("Scrape method must be implemented by subclasses")

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cierra el driver cuando se sale del bloque 'with'
        self.driver.quit()
    
    def get_data(self, url):
        return self.driver.get(url)
        return self.driver.get_page_source()

    def close(self):
        self.driver.quit()
