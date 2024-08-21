import subprocess
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
import logging
from .utils.scrapers import run_scraper



logger = logging.getLogger('django')

def index(request):
    return render(request, 'index.html')

def run_fill_form(request):
    return run_scraper(request, 'FillForm')

def run_table_scraper(request):
    return run_scraper(request, 'TableScrapper')