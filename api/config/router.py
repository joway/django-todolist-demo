from rest_framework import routers

from todo.apis import TodoItemViewSet, TodoListViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'item', TodoItemViewSet, base_name='item')
router.register(r'list', TodoListViewSet, base_name='list')
