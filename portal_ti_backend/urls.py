# portal_ti/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api import views
from api.views import create_link, create_programa, create_manual

router = routers.DefaultRouter()
router.register(r'links', views.LinkViewSet)
router.register(r'programas', views.ProgramaViewSet)
router.register(r'manuais', views.ManualViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/create_link/', create_link, name='create_link'),
    path('api/create_programa/', create_programa, name='create_programa'),
    path('api/create_manual/', create_manual, name='create_manual'),
]

# Adiciona rotas específicas para acessar os arquivos em DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.PROGRAMAS_URL, document_root=settings.PROGRAMAS_ROOT)
    urlpatterns += static(settings.MANUAIS_URL, document_root=settings.MANUAIS_ROOT)