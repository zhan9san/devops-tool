from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Deployment
from .serializers import DeploymentSerializer
from .tasks import send_dingtalk_message


class DeploymentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Deployment.objects.select_related('app', 'env').all()
    serializer_class = DeploymentSerializer
    # authentication_classes = (
    #     TokenAuthentication, SessionAuthentication,
    # )
    # permission_classes = (
    #     IsAuthenticated,
    # )

    def list(self, request, *args, **kwargs):
        send_dingtalk_message.delay(1, 2)
        return super().list(request, *args, **kwargs)
