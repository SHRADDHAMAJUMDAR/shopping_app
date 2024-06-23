# Generated by Django 5.0.2 on 2024-03-31 13:29

import django.db.models.deletion
import store.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
                ('p_desc', models.TextField()),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('img', models.ImageField(blank=True, null=True, upload_to=store.utilities.get_file_path)),
                ('on_sale', models.BooleanField(default=False)),
                ('saleprice', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('p_cat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]