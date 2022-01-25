# Generated by Django 2.1.5 on 2021-12-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_category_category_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_choices',
            field=models.CharField(choices=[('VG', 'veg'), ('NV', 'non-veg')], default='', max_length=2),
        ),
    ]