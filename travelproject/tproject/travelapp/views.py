from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import actors

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    act=actors.objects.all()
    return render(request,"index.html",{'result':obj,
                                        'res':act})
