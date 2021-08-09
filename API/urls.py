from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='Category')
router.register(r'offers', views.OffersViewSet, basename='Offers')

urlpatterns = [
    path('', include(router.urls)),
]
