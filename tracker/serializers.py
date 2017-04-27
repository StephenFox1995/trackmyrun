from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.gis.geos.collections import MultiLineString
from .models import Activity


class ActivitySerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Activity
        geo_field = 'route'
        id_field = False
        fields = ('route', 'start', 'end', 'created', 'owner_id', 'distance', 'activity_type')


    def calculate_distance(self, coordinates):
        m_string = MultiLineString(coordinates)
        return m_string.length


