from django.db import models
from django.utils.translation import gettext_lazy as _
from statuses.models import Statuses
from users.models import CustomUser


class Tasks(models.Model):
    name = models.CharField(_('Название задачи'), max_length=150)
    description = models.TextField(_('Описание'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Statuses,
                               on_delete=models.PROTECT,
                               related_name=_('Статусы'),
                               related_query_name=_('Статус'),
                               verbose_name=_('Статус'))
    author = models.ForeignKey(CustomUser,
                               on_delete=models.PROTECT,
                               related_name=_('Авторы'),
                               related_query_name=_('Автор'),
                               verbose_name=_('Автор'))
    executor = models.ForeignKey(CustomUser,
                                 on_delete=models.PROTECT,
                                 null=True,
                                 blank=True,
                                 related_name=_('Исполнители'),
                                 related_query_name=_('Исполнитель'),
                                 verbose_name=_('Исполнитель'))

    class Meta(object):
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')

    def __str__(self):
        return self.name
