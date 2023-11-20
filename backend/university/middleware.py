# import time
# import logging

# logger = logging.getLogger('main')

# class TestMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request, *args, **kwargs):
#         start_time = time.monotonic()
#         response = self.get_response(request, *args, **kwargs)
#         end_time = time.monotonic()

#         status_code = response.status_code
#         logger.debug(f"HTTP Status Code: {status_code} - View has been executing for: {end_time - start_time} seconds")

#         return response