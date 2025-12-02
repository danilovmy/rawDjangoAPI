"""
URL configuration for rawapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView, TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema.yaml", RedirectView.as_view(url=settings.MEDIA_URL + "schema.yaml")),
    path("docs/", TemplateView.as_view(template_name="swagger.html"), name="swagger"),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("api/v1/", include("api.urls", namespace="api")),
    #path("api/v2/", include("api.v2_urls", namespace="api_v2")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])