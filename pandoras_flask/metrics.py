import prometheus_client
import time

from flask import request, Response
from prometheus_client import multiprocess, Counter, Histogram

# Multiprocessing setup
# Cf. https://github.com/prometheus/client_python#multiprocess-mode-gunicorn
registry = prometheus_client.CollectorRegistry()
multiprocess.MultiProcessCollector(registry)

# Metrics for the `app` module - reads & writes

PING_RESPONSE = Counter('ping_response',
                        '/ping response codes', ['code'])

# Middleware / setup
# Following the Flask multiprocessing example in
# https://github.com/amitsaha/python-prometheus-demo

REQUEST_COUNT = Counter('request_count', 'App Request Count',
                        ['method', 'endpoint', 'http_status'])

REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request Latency',
                            ['endpoint'])


def start_timer():
    request.start_time = time.time()


def stop_timer(response):
    resp_time = time.time() - request.start_time
    REQUEST_LATENCY.labels(request.path).observe(resp_time)
    return response


def record_request_data(response):
    REQUEST_COUNT.labels(request.method, request.path,
                         response.status_code).inc()
    return response


# Cf. Prometheus exposition format in https://git.io/fpSOY
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')


def setup(app):
    app.before_request(start_timer)

    # `after_request` functions are executed in the reverse of the order
    # they were added. We want `stop_timer` to be executed first.
    app.after_request(record_request_data)
    app.after_request(stop_timer)

    @app.route('/metrics')
    def metrics():
        return Response(prometheus_client.generate_latest(registry),
                        mimetype=CONTENT_TYPE_LATEST)
