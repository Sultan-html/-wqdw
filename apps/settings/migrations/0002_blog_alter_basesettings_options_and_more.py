# Generated by Django 5.1.2 on 2024-10-13 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок блога')),
                ('description', models.TextField(verbose_name='Описание блога')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('comments', models.CharField(max_length=255, verbose_name='Комментарии')),
            ],
            options={
                'verbose_name': 'Запись блога',
                'verbose_name_plural': 'Записи блога',
            },
        ),
        migrations.AlterModelOptions(
            name='basesettings',
            options={'verbose_name': 'Основные настройки сайта', 'verbose_name_plural': 'Основные настройки сайта'},
        ),
        migrations.AlterField(
            model_name='basesettings',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='Ссылка на Facebook'),
        ),
        migrations.AlterField(
            model_name='basesettings',
            name='github',
            field=models.URLField(blank=True, verbose_name='Ссылка на Github'),
        ),
        migrations.AlterField(
            model_name='basesettings',
            name='google',
            field=models.URLField(blank=True, verbose_name='Ссылка на Google+'),
        ),
        migrations.AlterField(
            model_name='basesettings',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Логотип сайта'),
        ),
        migrations.AlterField(
            model_name='basesettings',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='Ссылка на Twitter'),
        ),
    ]