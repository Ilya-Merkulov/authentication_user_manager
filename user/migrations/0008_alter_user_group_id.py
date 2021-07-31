# Generated by Django 3.2.5 on 2021-07-31 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('user', '0007_alter_user_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='group.groups'),
        ),
    ]
