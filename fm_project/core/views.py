from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import User, Event
from .permissions import IsOwnerOrReadOnly, IsEventParticipant
from .serializers import UserSerializer, UserRegisterSerializer, EventSerializer, ChatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

#Users
class UsersList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, pk, slug):
        return get_object_or_404(User, pk=pk, slug=slug)
    def get(self, request, pk, slug, format=None):
        user = self.get_object(pk, slug)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserRegister(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Events
class EventList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EventDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, pk, slug):
        event = get_object_or_404(Event, pk=pk, slug=slug)
        self.check_object_permissions(self.request, event) 
        return event
    def get(self, request, pk, slug, format=None):
        event = self.get_object(pk, slug)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserEventList(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def get(self, request, pk, slug, format=None):
        user = get_object_or_404(User, pk=pk, slug=slug)
        events = Event.objects.filter(user=user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

#Chat for event participants  
class CreateChatMessage(APIView):
    permission_classes = [IsEventParticipant]
    def post(self, request, pk, slug, format=None):
        event = get_object_or_404(Event, pk=pk, slug=slug)
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user, event=event)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#добавить сообщение в чат события
    