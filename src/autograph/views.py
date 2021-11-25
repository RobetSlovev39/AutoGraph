from .services.core import update_schemas 
from django.http import HttpResponse, HttpRequest


def index_view(request: HttpRequest) -> HttpResponse:
    print(update_schemas())
    return HttpResponse('works')
