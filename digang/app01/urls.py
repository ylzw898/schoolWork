from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app01 import views

router = DefaultRouter()
router.register('book', views.BooksViewSet)
router.register('rent', views.RentViewSet)
router.register('housePrice', views.HousePriceViewSet)
router.register('userInformation', views.UserInformationViewSet)
router.register('check', views.CheckViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
