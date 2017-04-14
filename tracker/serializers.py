
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Activity


class ActivitySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Activity
        geo_field = 'route'
        fields = ('start', 'end', 'created', 'owner_id', 'activity_type')
