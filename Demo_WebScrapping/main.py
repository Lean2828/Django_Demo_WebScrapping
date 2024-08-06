import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Demo_WebScrapping.controllers.FillForm_controller import FillForm_controller
from Demo_WebScrapping.controllers.GetDataFromTables_controller import GetDataFromTables_controller

if __name__ == "__main__":
    # Obtener el modo de ejecución de la variable de entorno
    execution = os.getenv('SCRAPER_EXECUTION', 'FillForm')
    
    if execution == 'FillForm':
        form_filler_controller = FillForm_controller()
        form_filler_controller.run()

    if execution == 'TableScrapper':
        table_scraper_controller = GetDataFromTables_controller()
        table_scraper_controller.run()

