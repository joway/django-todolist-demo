from rest_framework import serializers

from todo.models import TodoItem, TodoList


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'content', 'done']


class TodoListSerializer(serializers.ModelSerializer):
    items = TodoItemSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ['id', 'name', 'items']


class TodoListUpdateSerializer(serializers.Serializer):
    items = serializers.ListField()
