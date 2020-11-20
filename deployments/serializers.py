from rest_framework import serializers
from deployments.models import Deployment
from applications.models import Application
from environments.models import Environment


class DeploymentSerializer(serializers.ModelSerializer):
    env = serializers.SlugRelatedField(queryset=Environment.objects.all(), slug_field='name')
    app = serializers.SlugRelatedField(queryset=Application.objects.all(), slug_field='name')

    class Meta:
        model = Deployment
        fields = (
            'url',
            'pk',
            'package',
            'ticket',
            'jenkins_build_url',
            'app',
            'env',
        )
