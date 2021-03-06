# Generated by Django 4.0.4 on 2022-06-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_items_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('deadline', models.TextField(verbose_name='Срок выполнения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('person', models.TextField(verbose_name='Ответственный')),
            ],
            options={
                'verbose_name': 'Поручение',
                'verbose_name_plural': 'Поручения',
            },
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Заявки', 'verbose_name_plural': 'Заявки'},
        ),
    ]
