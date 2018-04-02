# Generated by Django 2.0.3 on 2018-03-28 08:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_iucnstatus_taxon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('site', models.ManyToManyField(to='base.LocationSite')),
            ],
        ),
    ]
