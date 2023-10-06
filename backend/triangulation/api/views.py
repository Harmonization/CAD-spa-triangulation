from rest_framework.viewsets import ModelViewSet
from ..models import Triangulation
from .serializers import TriangleSerializer
from rest_framework.response import Response

from ..Geometry.triangulation import Triangulation as TriangulationGeometry
import json

class TriangulationViewSet(ModelViewSet):
    queryset = Triangulation.objects.all()
    serializer_class = TriangleSerializer
    
    def create(self, request):
        parameters =  json.loads(request.body)
        h, R, N = parameters['h'], parameters['R'], parameters['N']

        cone = TriangulationGeometry(h, R, N)
        cone.calculate_vertexes()
        triangle_points, normals_points = cone.get_points()
        
        return Response({'parameters': {'h': h, 'R': R, 'N': N}, 'points': triangle_points, 'normales': normals_points})