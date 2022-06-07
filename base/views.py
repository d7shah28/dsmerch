from django.shortcuts import render
from django.http import HttpResponse
import datetime

def test_page(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


# TODO write product landing page view