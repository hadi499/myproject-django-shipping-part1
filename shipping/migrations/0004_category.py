# Generated by Django 4.0.4 on 2022-05-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_alter_shipping_kategori_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
    ]
