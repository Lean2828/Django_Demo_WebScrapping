import subprocess
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
import logging
from .utils.scrapers import run_scraper
import os
import json



logger = logging.getLogger('django')

def index(request):
    json_path = os.path.join(settings.BASE_DIR, 'static', 'info_scrapers.json')
    with open(json_path, 'r') as f:
        scrapers = json.load(f)
    return render(request, 'index.html', {'scrapers': scrapers})

def run_fill_form(request):
    return run_scraper(request, 'FillForm')

def run_table_scraper(request):
    return run_scraper(request, 'TableScrapper')