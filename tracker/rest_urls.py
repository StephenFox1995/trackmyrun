from django.conf.urls import include, url
from rest_framework import routers
from tracker import rest_views


router = routers.DefaultRouter()
router.register('activity', rest_views.ActivityViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
