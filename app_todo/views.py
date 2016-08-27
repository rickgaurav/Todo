from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from app_todo.models import Todo
from app_todo.serializers import TodoSerializer, UserSerializer
from app_todo.permissions import IsOwnerOrReadOnly


class TodoListView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer







