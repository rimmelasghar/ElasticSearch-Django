from django.test import TestCase
from ..models import Products
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='Pujan', email='pujan@gmail.com', password='pujanpujan')

    def test_add_record_event(self):
        new_record = Products.objects.create(
            user=self.user, title='hello', description='hello hello')
        self.assertEqual(new_record.user.username, 'Pujan')
        self.assertEqual(new_record.title, 'hello')
        self.assertEqual(new_record.description, 'hello hello')