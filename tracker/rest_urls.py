from django.conf.urls import url
from tracker import rest_views


urlpatterns = [
    url(r'activity/', rest_views.ActivityRetrieveAPI.as_view(), name="activity"),
    url(r'^token-auth/$', rest_views.obtain_auth_token, name='obtain-token-auth'),
    url(r'^register', rest_views.register, name="register"),
]
