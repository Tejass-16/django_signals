from django.shortcuts import render
from django.http import HttpResponse
from .signals import my_signal
from .rectangle import Rectangle
from django.db import transaction
import threading

# Create your views here.

def test_signal_view(request):
    print(f"Caller is running in thread: {threading.current_thread().name}")
    with transaction.atomic():
        print("Before sending the signal")
        my_signal.send(sender=None)
        print("After sending the signal")
    return render(request, 'test_signal.html')

def test_rectangle_view(request):
    context={}

    rect = Rectangle(10, 5)
    result = []
    for item in rect:
        result.append(str(item))
    context['result']=result    
    return render(request, 'test_rectangle.html', context)
