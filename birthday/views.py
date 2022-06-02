from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.shortcuts import render
import datetime 

# Create your views here.
def index(reuqest):
    now = datetime.datetime.now()
    birthday = now.month == 9 and now.day == 27
    return render(reuqest, 'birthday/index.html', {'birthday': birthday })