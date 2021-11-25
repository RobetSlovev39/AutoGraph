# Generated by Django 3.2.9 on 2021-11-25 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autograph', '0004_devicegroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devicegroup',
            options={'verbose_name': 'Группу машин', 'verbose_name_plural': 'Группы машин'},
        ),
        migrations.AddField(
            model_name='devicegroup',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='devicegroup',
            name='name',
            field=models.CharField(help_text='Имя группы, машины которой будут обрабатываться', max_length=50, verbose_name='Название группы'),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('device_id', models.CharField(max_length=50, unique=True, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Включено')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='autograph.devicegroup', verbose_name='Группа')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='autograph.schema', verbose_name='Схема')),
            ],
        ),
    ]
