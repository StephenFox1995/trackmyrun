from django.conf.urls import url

from tracker import rest_views


urlpatterns = [
    url(r'activity/', rest_views.ActivityRetrieveAPI.as_view(), name="activity"),
    url(r'^tokenlogin/$', rest_views.token_login, name='token-login'),
]
