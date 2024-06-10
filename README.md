
# Django Performance Monitoring Project

This project is a Django application designed to monitor the performance of your system by logging request durations and other metrics.

## Table of Contents

1. [Installation]
2. [Configuration]
3. [Middleware Setup]
4. [Adding Performance Logging to Views]
5. [Analyzing Logs]
6. [Optional: Advanced Monitoring]

## Installation

1. Clone the Repository:
   git clone [<repository-url>](https://github.com/YENG-SEBASTIAN/djangp-logging-tutorials.git)
   cd performance_monitor

2. Create and Activate a Virtual Environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:
   pip install -r requirements.txt

4. Start a New Django Project and App:
   django-admin startproject performance_monitor .
   python manage.py startapp monitor

## Configuration

1. Update `settings.py` for Logging:
   Add the following logging configuration to your `performance_monitor/settings.py` file:
   
   ```python
   import os

   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'formatters': {
           'verbose': {
               'format': '{levelname} {asctime} {module} {message}',
               'style': '{',
           },
           'simple': {
               'format': '{levelname} {message}',
               'style': '{',
           },
       },
       'handlers': {
           'file': {
               'level': 'DEBUG',
               'class': 'logging.FileHandler',
               'filename': os.path.join(BASE_DIR, 'performance.log'),
               'formatter': 'verbose',
           },
       },
       'loggers': {
           'my_django_monitor': {
               'handlers': ['file'],
               'level': 'DEBUG',
               'propagate': True,
           },
       },
   }
   ```

## Middleware Setup

1. Create Performance Monitoring Middleware:
   Create a file `monitor/middleware.py` and add the following code:

   ```python
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
   ```

2. **Add Middleware to `settings.py`**:
   Update the `MIDDLEWARE` setting in `performance_monitor/settings.py` to include the performance monitoring middleware:

   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'django.contrib.sessions.middleware.SessionMiddleware',
       'django.middleware.common.CommonMiddleware',
       'django.middleware.csrf.CsrfViewMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       'django.contrib.messages.middleware.MessageMiddleware',
       'django.middleware.clickjacking.XFrameOptionsMiddleware',
       'monitor.performance_middleware.PerformanceMonitoringMiddleware',  # Add this line
   ]
   ```

## Adding Performance Logging to Views

1. **Log Performance in Views**:
   Add performance logging to your views for more detailed monitoring. For example, in `monitor/views.py`:

   ```python
   from django.http import HttpResponse
   import logging
   import time

   logger = logging.getLogger('django')

   def example_view(request):
       start_time = time.time()
       # Your view logic here
       duration = time.time() - start_time
       logger.debug(f'example_view took {duration:.4f} seconds')
       return HttpResponse('Hello, world!')
   ```

## Analyzing Logs

1. View Logs:
   The performance logs will be saved in the `performance.log` file located in the base directory of your project. You can open this file to view the logged performance data.

2. Log Rotation:
   To manage log file sizes, consider using log rotation. You can use `logging.handlers` such as `RotatingFileHandler` for this purpose.

## Optional: Advanced Monitoring

1. Integrate with Monitoring Tools:
   For more advanced monitoring capabilities, you can integrate with tools like Prometheus, Grafana, or New Relic.

2. Use Django Extensions for Detailed Profiling:
   Consider using `django-silk` for detailed performance profiling.

   ```sh
   pip install django-silk
   ```

   Add `'silk'` to `INSTALLED_APPS` in `performance_monitor/settings.py` and include its middleware:

   ```python
   MIDDLEWARE += ['silk.middleware.SilkyMiddleware']
   ```

   Run migrations and access the Silk dashboard:

   ```sh
   python manage.py migrate
   ```

   Visit `/silk/` in your browser to see detailed performance metrics.

## Conclusion

This setup will help you monitor the performance of your Django application by logging request durations and other metrics. You can extend this further by integrating additional monitoring tools and logging more specific data as needed.
