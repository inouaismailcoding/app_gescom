# Generated by Django 3.2.16 on 2023-11-02 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0004_auto_20231101_1058'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mouvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mouvement', models.CharField(blank=True, choices=[('IN', 'IN'), ('OUT', 'OUT')], max_length=20, null=True, verbose_name='Mouvement')),
                ('motif', models.CharField(blank=True, max_length=50, null=True, verbose_name='Motif')),
                ('description', models.TextField(blank=True, max_length=20, null=True, verbose_name='Description Mouvement')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='reference Vente')),
                ('date', models.DateTimeField(auto_now=True)),
                ('mouvement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.mouvement')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.article')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='transaction.transaction')),
            ],
        ),
    ]