from Demo_WebScrapping.controllers.FillForm_controller import FillForm_controller
from Demo_WebScrapping.controllers.GetDataFromTables_controller import GetDataFromTables_controller

def main(execution):
    if execution == 'FillForm':
        form_filler_controller = FillForm_controller()
        form_filler_controller.run()

    elif execution == 'TableScrapper':
        table_scraper_controller = GetDataFromTables_controller()
        table_scraper_controller.run()

if __name__ == "__main__":
    execution = 'FillForm'
    main(execution)
