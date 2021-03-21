from django.db import models
from django.utils.translation import gettext_lazy as _


class Statuses(models.Model):
    name = models.CharField(_('Название статуса'), max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        verbose_name = _('Статус')
        verbose_name_plural = _('Статусы')

    def __str__(self):
        return self.name
