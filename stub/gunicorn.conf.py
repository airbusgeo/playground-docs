"""Gunicorn (http server) configuration.
"""

import multiprocessing

worker_class = 'sync'
workers = multiprocessing.cpu_count() * 2 + 1
#timeout = 60

