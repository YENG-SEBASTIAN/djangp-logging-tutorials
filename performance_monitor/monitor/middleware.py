import time
import logging
from prometheus_client import Summary, start_http_server



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



REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

class PrometheusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        start_http_server(8000)  # Prometheus metrics available at http://localhost:8000

    @REQUEST_TIME.time()
    def __call__(self, request):
        response = self.get_response(request)
        return response
