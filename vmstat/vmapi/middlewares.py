from django.http import QueryDict


def put_middleware(get_response):
    def middleware(request):
        if request.method == "PUT":
            setattr(request, "PUT", QueryDict(request.body))
        response = get_response(request)
        return response

    return middleware
