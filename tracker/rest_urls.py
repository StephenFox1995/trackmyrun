from django.conf.urls import url
from tracker import rest_views


urlpatterns = [
    url(r'activity$', rest_views.activity, name="activity"),
    url(r'activity/owner/(?P<owner_id>[0-9]+)$', rest_views.get_activities_for_user, name="get_activities_for_user"),
    url(r'^token-auth/$', rest_views.obtain_auth_token, name='obtain-token-auth'),
    url(r'^register', rest_views.register, name="register"),
]
