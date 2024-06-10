import time
import logging

logger = logging.getLogger('my_django_monitor')

class PerformanceMonitoringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time

        logger.debug(f'{request.method} {request.path} took {duration:.4f} seconds')

        return response
