from django.shortcuts import render

# Create your views here.

def make_order(request):
    return render(request, 'order.html')