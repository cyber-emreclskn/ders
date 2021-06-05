# Generated by Django 3.1.7 on 2021-05-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20210528_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlandi'), ('deleted', 'Silindi')], default='draft', max_length=10)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='carousel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upadated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
