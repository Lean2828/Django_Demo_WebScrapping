import subprocess
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
import sys
import platform

def index(request):
    return render(request, 'index.html')

def run_fill_form(request):
    # Path to your main.py script
    script_path = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'Demo_WebScrapping', 'main.py'))

  # Detect the operating system
    if platform.system() == 'Windows':
        # Path to the Python executable in the virtual environment (Windows)
        python_executable = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'VENV_Django_WebScrapping', 'Scripts', 'python.exe'))
    else:
        # Path to the Python executable in the virtual environment (Unix/Linux)
        python_executable = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'VENV_Django_WebScrapping', 'bin', 'python'))

    # Set the execution variable for FillForm
    env = os.environ.copy()
    env['SCRAPER_EXECUTION'] = 'FillForm'
    env['PYTHONPATH'] = os.path.abspath(os.path.join(settings.BASE_DIR, '..'))

    # Run the script
    result = subprocess.run([python_executable, script_path], env=env, capture_output=True, text=True)

    # Handle the result
    if result.returncode == 0:
        return HttpResponse("FillForm scraper executed successfully")
    else:
        return HttpResponse(f"Error: {result.stderr}")

def run_table_scraper(request):
    # Path to your main.py script
    script_path = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'Demo_WebScrapping', 'main.py'))

  # Detect the operating system
    if platform.system() == 'Windows':
        # Path to the Python executable in the virtual environment (Windows)
        python_executable = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'VENV_Django_WebScrapping', 'Scripts', 'python.exe'))
    else:
        # Path to the Python executable in the virtual environment (Unix/Linux)
        python_executable = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'VENV_Django_WebScrapping', 'bin', 'python'))

    # Set the execution variable for TableScrapper
    env = os.environ.copy()
    env['SCRAPER_EXECUTION'] = 'TableScrapper'
    env['PYTHONPATH'] = os.path.abspath(os.path.join(settings.BASE_DIR, '..'))

    # Run the script
    result = subprocess.run([python_executable, script_path], env=env, capture_output=True, text=True)

    # Handle the result
    if result.returncode == 0:
        return HttpResponse("TableScrapper executed successfully")
    else:
        return HttpResponse(f"Error: {result.stderr}")
