from rest_framework import serializers
from app_todo.models import Todo
from django.contrib.auth.models import User


class TodoSerializer(serializers.HyperlinkedModelSerializer):

    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Todo
        fields = ('url', 'id', 'content', 'created_date', 'completed', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    created_todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'created_todos')