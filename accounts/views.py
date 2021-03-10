import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserDisplaySerializer

logger = logging.getLogger(__name__)


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        logger.info("%s", request.user)
        return Response(serializer.data)
