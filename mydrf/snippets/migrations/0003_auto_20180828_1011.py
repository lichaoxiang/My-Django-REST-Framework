# Generated by Django 2.0.6 on 2018-08-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20180828_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('css', 'CSS'), ('html', 'HTML'), ('python', 'Python'), ('php', 'PHP')], default='python', max_length=100),
        ),
    ]
