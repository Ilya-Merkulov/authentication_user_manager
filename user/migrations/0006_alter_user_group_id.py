# Generated by Django 3.2.5 on 2021-07-31 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('user', '0005_auto_20210730_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group_id',
            field=models.ForeignKey(default='null', null=True, on_delete=django.db.models.deletion.CASCADE, to='group.groups'),
        ),
    ]
