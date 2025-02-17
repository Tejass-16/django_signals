1. Django Signals
Question 1: Are Django signals executed synchronously or asynchronously by default?
By default, Django signals are executed synchronously. This means that when a signal is sent, the associated signal handlers are executed immediately, and the program waits for them to finish before proceeding.
Explanation
The signal handler (my_signal_handler) runs immediately after the signal is sent.

The program waits for the handler to complete before printing "After sending the signal".

Question 2: Do Django signals run in the same thread as the caller?
Yes, Django signals run in the same thread as the caller. This can be verified by checking the thread name in both the caller and the signal handler.
Explanation
Both the caller and the signal handler run in the same thread (MainThread).

This confirms that signals do not spawn new threads by default.

Question 3: Do Django signals run in the same database transaction as the caller?
Yes, Django signals run in the same database transaction as the caller by default. If the transaction is rolled back, any changes made by the signal handler are also rolled back.
Explanation
The signal handler runs within the same transaction as the caller.

If the transaction fails, the database operation in the signal handler is also rolled back.

Question 4: Create a Rectangle class with iteration support
The Rectangle class is designed to be initialized with length and width. It supports iteration, yielding the length and width in a specific format.
Explanation
The Rectangle class is initialized with length and width.

The __iter__ and __next__ methods allow the class to be iterated over.

During iteration, it first yields the length in the format {'length': <value>} and then the width in the format {'width': <value>}.
