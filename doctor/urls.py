from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('designation', views.DesignationViewSet)
router.register('specalaization', views.SpecializationViewSet)
router.register('reviwe', views.ReviewViewSet)
router.register('available_time', views.AvailableTimeViewSet)
router.register('list', views.DoctorViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
