import json

from django.urls import reverse

from utils.testing import BaseAPITesting


class TodoTest(BaseAPITesting):
    def setUp(self):
        super(TodoTest, self).setUp()
        self.list_name = 'test list'
        self.list_id = 1

    def test_create_todo_list(self):
        path = reverse('api:list-list')
        ret = self.client.post(path, data={
            'name': self.list_name,
        })
        self.assertTrue(ret.status_code == 201)

    def test_delete_todo_list(self):
        self.test_create_todo_list()
        path = reverse('api:list-list')
        ret = self.client.delete('{0}/{1}'.format(path, self.list_name))
        self.assertTrue(ret.status_code == 204)

    def test_append_todo_item(self):
        self.test_create_todo_list()
        # create item
        path = reverse('api:item-list')
        ret = self.client.post(path, data={
            'content': 'test item',
        })
        item = ret.json()
        self.assertTrue(ret.status_code == 201)

        # append item into list
        path = reverse('api:list-list')
        ret = self.client.put('{0}/{1}'.format(path, self.list_name), data={
            'items': [item['id'], ]
        })
        self.assertTrue(ret.status_code == 200)

        # get todolist
        path = reverse('api:list-list')
        ret = self.client.get('{0}/{1}'.format(path, self.list_name))
        self.assertTrue(ret.status_code == 200)
        self.assertEqual(ret.json()['items'][0]['id'], item['id'])
