import logging
from Demo_WebScrapping import main as scraper_main
from django.http import HttpResponse
from django.conf import settings

logger = logging.getLogger('django')

def run_scraper(request, scraper_name):
    if not settings.IS_LOCAL:
        return HttpResponse('This feature is available only for local environments. Contact me to request a live demo.', status=403)

    try:
        # Llamada directa al main.py con el parámetro correspondiente
        scraper_main.main(scraper_name)
        
        # Log de éxito
        logger.info(f"{scraper_name} scraper executed successfully")
        return HttpResponse(f"{scraper_name} scraper executed successfully")
    except Exception as e:
        logger.error(f"Error during execution: {str(e)}")
        return HttpResponse(f"Error: {str(e)}", status=500)
