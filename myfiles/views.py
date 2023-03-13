import datetime

from django.shortcuts import render
from myfiles.models import Portfolio, Murojaat
# Create your views here.

def index(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        message = request.POST.get('message')
        vaqt = datetime.datetime.now()
        Murojaat(ism=name, email=email, sub=sub, text=message, date=vaqt).save()
    port = Portfolio.objects.all()
    return render(request, 'index.html', {'works': port})