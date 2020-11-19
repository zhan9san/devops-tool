from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Deployment, CurrentPackage


class CurrentPackageListView(LoginRequiredMixin, ListView):
    queryset = Deployment.objects.filter(status=True).select_related('env', 'app')
    context_object_name = 'packages'
    template_name = 'deployments/current_package_list.html'
    login_url = 'login'


class DeploymentListView(LoginRequiredMixin, ListView):
    queryset = Deployment.objects.filter(status=True).select_related('env', 'app')
    context_object_name = 'packages'
    template_name = 'deployments/deployment_list.html'
    login_url = 'login'
