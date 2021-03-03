"""DevOpsTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from deployments.apis import DeploymentViewSet
from .settings import DEBUG


class ClaimTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class ClaimTokenObtainPairView(TokenObtainPairView):
    serializer_class = ClaimTokenObtainPairSerializer

router = DefaultRouter()
router.register(r'deployments', DeploymentViewSet)

urlpatterns = [
    # Django admin
    path('bright/', admin.site.urls),

    # User management
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('pages.urls')),
    path('deployments/', include('deployments.urls')),
    path('api/', include(router.urls)),
    path("api/", include("accounts.urls")),

    path("api-auth/", include("rest_framework.urls")),
    path('api/token/', ClaimTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
