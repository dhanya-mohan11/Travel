from django.shortcuts import render

from .models import Destination
from .serializers import DestinationSerializer

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from rest_framework import generics

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import exception_handler

# Create your views here.


# def index(request):
#     return render(request,"index.html")


class ListDestinationAPIView(ListAPIView):
    queryset = Destination.objects.all().order_by('-created_at')
    serializer_class = DestinationSerializer

   
class CreateDestinationAPIView(CreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class RetrieveDestinationAPIView(RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class UpdateDestinationAPIView(UpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestroyDestinationAPIView(DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


# OR

'''
class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

'''


class CustomAuthTokenLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
    
    
def my_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now customize the response with your own error message
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['message'] = 'Not found !!'

    return response