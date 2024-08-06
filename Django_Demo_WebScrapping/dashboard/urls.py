from django.urls import path
from .views import run_fill_form,run_table_scraper, index

urlpatterns = [
    path('', index, name='index'),
    path('run-fill-form/', run_fill_form, name='run_fill_form'),
    path('run-table-scraper/', run_table_scraper, name='run_table_scraper'),
]
