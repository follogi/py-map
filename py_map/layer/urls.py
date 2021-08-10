from django.urls.conf import path
from layer.views import TileMapService, WebMapService

urlpatterns = [
    path('tms/', view=TileMapService.as_view(), name='tms'),
    path('wms/', view=WebMapService.as_view(), name='wms'),
]
