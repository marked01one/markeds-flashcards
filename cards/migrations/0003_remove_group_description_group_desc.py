# Generated by Django 4.0.4 on 2022-10-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_group_card_group_name_alter_card_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.AddField(
            model_name='group',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=280),
        ),
    ]
