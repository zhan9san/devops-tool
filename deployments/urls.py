from django.urls import path
from .views import DeploymentListView, CurrentPackageListView

urlpatterns = [
    path('', DeploymentListView.as_view(), name='deployment_list'),
    path('current/', CurrentPackageListView.as_view(), name='current_package_list'),
]
