from django.dispatch import Signal, receiver
from django.db import transaction
import threading
from .models import MyModel

# Create a signal
my_signal = Signal()

# Define a signal receiver
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler is running...")
    print(f"Signal handler is running in thread: {threading.current_thread().name}")
    # Simulate a database operation
    MyModel.objects.create(name="Test")