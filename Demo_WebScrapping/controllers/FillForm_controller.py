from Demo_WebScrapping.controllers.BaseController import BaseController
from Demo_WebScrapping.scrapers.Demo_FillForm import DemoFillFormScrapper

class FillForm_controller(BaseController):
    def __init__(self):
        scraper = DemoFillFormScrapper()
        super().__init__(scraper)
