# Generated by Django 2.1.5 on 2021-12-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20211230_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_choices',
            field=models.CharField(choices=[('VG', 'veg'), ('NV', 'non-veg')], default='', max_length=2),
        ),
    ]