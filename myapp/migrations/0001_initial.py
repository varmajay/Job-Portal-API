# Generated by Django 4.0.5 on 2022-06-09 03:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(default='hr', max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], default=None, null=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('profile', models.FileField(default='profile.png', upload_to='user')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', myapp.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('marketing', 'Marketing'), ('customer service', 'Customer Service'), ('human resource', 'Human Resource'), ('project management', 'Project Management'), ('business devlopment', 'Business Devlopment'), ('sales & communication', 'Seles & Communication'), ('teaching & education', 'Teaching & Education'), ('information technology', 'Information Technology')], max_length=50)),
                ('type', models.CharField(choices=[('full-time', 'Full-Time'), ('part-time', 'Part-Time'), ('internship', 'Internship')], max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('experience', models.CharField(max_length=50)),
                ('vacancy', models.IntegerField()),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('hr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('address', models.TextField()),
                ('resume', models.FileField(upload_to='resume')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jobs')),
            ],
        ),
    ]
