# Generated by Django 2.1.3 on 2018-11-13 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('language', models.CharField(choices=[('Python', 1), ('Java', 2), ('PHP', 3)], default='python', max_length=100)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
