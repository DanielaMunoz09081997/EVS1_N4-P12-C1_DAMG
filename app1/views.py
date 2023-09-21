from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1vista1(request):
    html="""
        <h1 style="color:blue">Hola mundo desde app1 vista 1</h1>
    """
    return HttpResponse(html)

def app2vista2(request):
    html="""
        <h1 style="color:red">Hola mundo desde app1 vista2</h1>
    """
    return HttpResponse(html)
