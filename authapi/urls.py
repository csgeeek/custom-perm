from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.StudentModelViewSet)
# router.register(r'snippets', views.StudentModelViewSetForAdmins,
#                 basename="snippets")
# router.register(r'users', views.StudentModelViewSetForOthers, basename="users")


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('auth/', include(router.urls)),
]
