from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class BaseAPITesting(APITestCase):
    def setUp(self):
        # create user
        self.email = 'jack@gmail.com'
        self.username = 'jack'
        self.password = 'passowrd123'
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_superuser(
            email=self.email,
            username=self.username,
            password=self.password
        )
