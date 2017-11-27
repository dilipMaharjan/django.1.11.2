from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    html_ = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <h1>Django 1.11.2</h1>
    </body>
    </html>
    """
    # return HttpResponse("Django 1.11.2")
    return HttpResponse(html_)
