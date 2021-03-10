import time
import logging


logger = logging.getLogger(__name__)


class PerformanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response['X-Page-Duration-ms'] = int(duration * 1000)
        logger.info("%s %s %s", duration, request.path, request.GET.dict())
        return response
