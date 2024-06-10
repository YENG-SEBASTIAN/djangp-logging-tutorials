from django.http import HttpResponse
import logging
import time

# Get the logger for your Django monitoring
logger = logging.getLogger('my_django_monitor')

# Define the view
def example_view(request):
    # Start the timer
    start_time = time.time()

    # View logic goes here
    # Simulating some processing with time.sleep (remove this in your actual logic)
    time.sleep(1)  # Replace this with your actual view logic

    # Calculate the duration
    duration = time.time() - start_time

    # Log messages at different levels
    logger.debug(f'This is a debug message: example_view took {duration:.4f} seconds')
    logger.info('This is an info message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

    # Return the response
    return HttpResponse('Hello, world!')
