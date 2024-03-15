from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from django.contrib.auth import login 
from .models import Event
from .serializers import EventSerializer, LoginSerializer, SignupSerializer

# Create your views here.

class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"detail": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupAPIView(APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListEvent(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ListEventParticularUser(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)


class CreateEvent(generics.CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)