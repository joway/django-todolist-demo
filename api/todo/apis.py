from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from todo.models import TodoItem, TodoList
from todo.serializers import TodoItemSerializer, TodoListSerializer, TodoListUpdateSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()
    permission_classes = (AllowAny,)


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    lookup_field = 'name'
    permission_classes = (AllowAny,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TodoListUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        items = [TodoItem.objects.get(id=item_id) for item_id in data['items']]
        instance.items = items
        instance.save()
        return Response(self.get_serializer(instance).data)
