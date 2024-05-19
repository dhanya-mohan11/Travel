from django.urls import path, include
from .views import (
    ListDestinationAPIView,
    CreateDestinationAPIView,
    RetrieveDestinationAPIView,
    UpdateDestinationAPIView,
    DestroyDestinationAPIView
)

from rest_framework import routers
from destinations import views

# router = routers.DefaultRouter()
# router.register('destinations', views.ListDestinationAPIView)

from rest_framework.authtoken import views

urlpatterns = [
    # path('', include(router.urls)),

    # path('',views.CustomAuthTokenLogin.as_view),
    
    path('destinations/', ListDestinationAPIView.as_view(), name='destinations-list'),
    path('destinations/create/', CreateDestinationAPIView.as_view(), name='destinations-create'),
    path('destinations/retrieve/<pk>', RetrieveDestinationAPIView.as_view(), name='destinations-retrieve'),
    path('destinations/update/<pk>', UpdateDestinationAPIView.as_view(), name='destinations-update'),
    path('destinations/destroy/<pk>', DestroyDestinationAPIView.as_view(), name='destinations-destroy'),

]