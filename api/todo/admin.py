from django.contrib import admin

from todo.models import TodoItem, TodoList


@admin.register(TodoItem)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'done', 'created_at')


@admin.register(TodoList)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'items', 'created_at')
