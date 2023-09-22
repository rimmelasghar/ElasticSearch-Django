from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Products(models.Model):

    class Meta:
        db_table = 'Products'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_uploaded = models.DateField(default=datetime.datetime.now())
    time_uploaded = models.TimeField(default=datetime.datetime.now())

    def __str__(self) -> str:
        return self.title