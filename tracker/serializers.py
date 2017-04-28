from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer
from .models import Activity, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ActivitySerializer(GeoFeatureModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        geo_field = 'route'
        id_field = False
        fields = ('route', 'start', 'end', 'created', 'owner_id', 'distance', 'activity_type', 'owner')


