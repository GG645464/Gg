# Generated by Django 2.0 on 2020-10-10 08:23

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.TextField(max_length=15)),
                ('gdate', models.DateTimeField(auto_now=True)),
                ('ggirlnum', models.IntegerField(default=0)),
                ('gboynum', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'grades',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.TextField(max_length=15)),
                ('sgender', models.BooleanField(default=True)),
                ('sage', models.IntegerField()),
                ('scontend', models.TextField(max_length=15)),
                ('isDelete', models.BooleanField(default=False)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.Grades')),
            ],
            options={
                'db_table': 'students',
                'ordering': ['-id'],
            },
            managers=[
                ('stuObj', django.db.models.manager.Manager()),
            ],
        ),
    ]
