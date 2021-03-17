from django.db import models


class User(models.Model):
    username = models.CharField('Username пользователя', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    password1 = models.CharField('Пароль', max_length=32)
    password2 = models.CharField('Подтверждение пароля', max_length=32)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
