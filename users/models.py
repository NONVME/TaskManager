from django.db import models


class User(models.Model):
    user_name = models.CharField('Имя пользователя', max_length=50)
    full_name = models.CharField('Полное имя', max_length=50)
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
