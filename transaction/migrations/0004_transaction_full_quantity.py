# Generated by Django 3.2.16 on 2023-11-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_intervenant_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='full_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
