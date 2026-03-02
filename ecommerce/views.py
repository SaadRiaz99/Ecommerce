from django.shortcuts import render , HttpResponse , redirect


def home(request):
    return render(request  , 'home.html')
def shop(request):
    return render(request  , 'shop.html')




