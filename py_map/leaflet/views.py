from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    """
    Render the leaflet map
    """
    context = {
        'host': '{scheme}://{host}/layer/'.format(scheme=request.scheme, host=request.get_host())
    }
    return render(request, 'leaflet/index.html', context)
