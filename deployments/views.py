from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Deployment, CurrentPackage


class CurrentPackageListView(LoginRequiredMixin, ListView):
    model = CurrentPackage
    context_object_name = 'packages'
    template_name = 'deployments/current_package_list.html'
    login_url = 'login'


class DeploymentListView(LoginRequiredMixin, ListView):
    model = Deployment
    context_object_name = 'packages'
    template_name = 'deployments/deployment_list.html'
    login_url = 'login'
