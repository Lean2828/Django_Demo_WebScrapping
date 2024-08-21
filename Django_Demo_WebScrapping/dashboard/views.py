import subprocess
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
import os
import sys
import platform
import logging
import datetime
from Demo_WebScrapping import main as scraper_main



logger = logging.getLogger('django')

def index(request):
    return render(request, 'index.html')

def run_fill_form(request):
    if not settings.IS_LOCAL:
        return HttpResponse('This feature is available only for local executions or with a subscription.', status=403)

    try:
        # Llamada directa al main.py con el parámetro 'FillForm'
        scraper_main.main('FillForm')
        
        # Log de éxito
        logger.info("FillForm scraper executed successfully")
        return HttpResponse("FillForm scraper executed successfully")
    except Exception as e:
        logger.error(f"Error during execution: {str(e)}")
        return HttpResponse(f"Error: {str(e)}", status=500)

def run_table_scraper(request):
    if not settings.IS_LOCAL:
        return HttpResponse('This feature is available only for local executions or with a subscription.', status=403)

    try:
        # Llamada directa al main.py con el parámetro 'TableScrapper'
        scraper_main.main('TableScrapper')
        
        # Log de éxito
        logger.info("TableScrapper executed successfully")
        return HttpResponse("TableScrapper executed successfully")
    except Exception as e:
        logger.error(f"Error during execution: {str(e)}")
        return HttpResponse(f"Error: {str(e)}", status=500)
