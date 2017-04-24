from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_gis.fields import GeometryField
# from rest_framework_gis.fields import GeoJsonDict
from .models import Activity


class ActivitySerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Activity
        geo_field = 'route'
        id_field = False
        fields = ('route', 'start', 'end', 'created', 'owner_id', 'activity_type')



