from django.contrib import admin

from todo.models import TodoItem, TodoList


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'done', 'created_at')


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
