# Generated by Django 3.1.7 on 2021-03-15 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_destroy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='destroy',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='furniture',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destroy',
            name='date',
            field=models.DateField(verbose_name='Destroy Date'),
        ),
        migrations.AlterField(
            model_name='destroy',
            name='supply',
            field=models.CharField(choices=[('S', 'Sledge hammer'), ('B', 'Bat'), ('C', 'Chainsaw')], default='S', max_length=1, verbose_name='Pick Your Destroy Object!'),
        ),
        migrations.AddField(
            model_name='furniture',
            name='finish',
            field=models.ManyToManyField(to='main_app.Finish'),
        ),
    ]