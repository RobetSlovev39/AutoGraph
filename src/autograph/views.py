from .services.core import update_devices
from django.http import HttpResponse, HttpRequest


def index_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('works')
