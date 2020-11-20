from rest_framework import viewsets

from .models import Deployment
from .serializers import DeploymentSerializer


class DeploymentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer
