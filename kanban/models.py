from django.db import models

from django.contrib.auth.models import User
from django.db import models


class List(models.Model) :

    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

########  カード作成機能の実装 models 作成
class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) ### 外部キー  User
    list = models.ForeignKey(List, on_delete=models.CASCADE) ### 外部キー  List

    def __str__(self):
        return self.title


