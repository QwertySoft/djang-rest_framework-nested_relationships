# Generated by Django 2.1.3 on 2018-11-13 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('PYTHON', 'Python'), ('JAVA', 'Java'), ('PHP', 'PHP')], default='python', max_length=100),
        ),
    ]
