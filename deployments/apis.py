from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Deployment
from .serializers import DeploymentSerializer


class DeploymentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer
    # authentication_classes = (
    #     TokenAuthentication, SessionAuthentication,
    # )
    permission_classes = (
        IsAuthenticated,
    )
