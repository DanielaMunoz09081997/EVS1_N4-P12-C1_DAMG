from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2vista1(request):
    html="""
        <h1 style="color:green">Hola mundo desde app2 vista 1</h1>
    """
    return HttpResponse(html)

def app2vista2(request):
    html="""
        <h1 style="color:yelow">Hola mundo desde app2 vista2</h1>
    """
    return HttpResponse(html)
