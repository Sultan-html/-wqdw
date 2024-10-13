from django.db import models

class BaseSettings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип сайта',
        blank=True,
        null=True
    )
    facebook = models.URLField(
        verbose_name='Ссылка на Facebook',
        blank=True
    )
    twitter = models.URLField(
        verbose_name='Ссылка на Twitter',
        blank=True
    )
    github = models.URLField(
        verbose_name='Ссылка на Github',
        blank=True
    )
    google = models.URLField(
        verbose_name='Ссылка на Google+',
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основные настройки сайта'
        verbose_name_plural = 'Основные настройки сайта'


class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок блога'
    )
    description = models.TextField(
        verbose_name='Описание блога'
    )
    image = models.ImageField(
        upload_to='image/',
        blank=True,
        null=True
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    comments = models.CharField(
        max_length=255,
        verbose_name='Комментарии'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
