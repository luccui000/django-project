# Generated by Django 2.2.6 on 2019-12-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieude', models.CharField(max_length=120)),
                ('motasp', models.TextField()),
                ('giasp', models.DecimalField(decimal_places=2, default=100000.0, max_digits=20)),
            ],
        ),
    ]