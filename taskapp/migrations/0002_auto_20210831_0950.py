# Generated by Django 3.2.6 on 2021-08-31 04:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Question'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ans',
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskapp.question'),
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2021, 8, 31, 4, 20, 2, 848385, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address '),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Question', to='taskapp.category'),
        ),
    ]
