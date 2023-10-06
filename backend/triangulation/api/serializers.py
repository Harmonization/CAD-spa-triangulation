from rest_framework.serializers import ModelSerializer
from ..models import Triangulation

class TriangleSerializer(ModelSerializer):
    class Meta:
        model = Triangulation
        fields = ('id', 'h', 'R', 'N')