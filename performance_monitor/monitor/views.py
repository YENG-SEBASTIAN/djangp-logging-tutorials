from django.http import HttpResponse
import logging
import time

logger = logging.getLogger('my_django_monitor')

def example_view(request):
    start_time = time.time()
    # Your view logic here
    duration = time.time() - start_time
    logger.debug(f'example_view took {duration:.4f} seconds')
    return HttpResponse('Hello, world!')
