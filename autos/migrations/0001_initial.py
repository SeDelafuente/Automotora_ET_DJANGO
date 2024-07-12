# Generated by Django 5.0.7 on 2024-07-12 09:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='Unknown Brand', max_length=100)),
                ('model', models.CharField(default='Unknown Model', max_length=100)),
                ('year', models.IntegerField(default=2000)),
                ('price', models.DecimalField(decimal_places=0, default=0.0, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
