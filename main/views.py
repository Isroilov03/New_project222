from django.shortcuts import render
from .models import *
# Create your views here.

def index_view(request):
    context = {
        "talabalar" : Client.objects.all()
    }
    return render(request, 'index.html', context)


print("salom")
print("salom")
print("salom")
print("salom")
