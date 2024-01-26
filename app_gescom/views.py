from django.shortcuts import render
from django.http import HttpResponse
from stock.functions import get_data_table_file
from stock.models import *


        #return get_data_table_file(request,Article) 