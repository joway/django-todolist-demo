from django.db import models


class TodoItem(models.Model):
    content = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)


class TodoList(models.Model):
    name = models.CharField(max_length=56, blank=True, unique=True)
    items = models.ManyToManyField(to=TodoItem, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
