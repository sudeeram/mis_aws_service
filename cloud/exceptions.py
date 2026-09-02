from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None: return None
    request = context.get("request")
    message = response.data.get("detail", "Request failed") if isinstance(response.data, dict) else "Request failed"
    response.data = {"error": {
        "code": getattr(exc, "default_code", "request_failed"),
        "message": str(message),
        "correlationId": getattr(request, "correlation_id", None),
    }}
    return response

