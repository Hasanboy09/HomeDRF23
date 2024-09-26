# Generated by Django 5.1.1 on 2024-09-25 17:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('All_property', 'all_property'), ('Rent', 'rent'), ('Home', 'home'), ('Business', 'business')], default='All_property', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Yard', 'yard'), ('Dacha', 'dacha'), ('Cottage', 'cottage')], default='Yard', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_sale', models.CharField(max_length=255)),
                ('for_rent', models.CharField(max_length=255)),
            ],
        ),
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
                ('email', models.EmailField(max_length=254, unique=True)),
                ('organization', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('balance', models.IntegerField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='advertisements/')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='apps.home')),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='home_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homes', to='apps.homecategory'),
        ),
        migrations.CreateModel(
            name='HomeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='apps.home')),
            ],
        ),
        migrations.CreateModel(
            name='HomeNeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_count', models.IntegerField()),
                ('length', models.FloatField()),
                ('price', models.FloatField()),
                ('floor', models.IntegerField()),
                ('build_with', models.CharField(max_length=255)),
                ('repair', models.CharField(choices=[('Middle', 'middle'), ('Euro', 'euro'), ('Without_Repair', 'without_repair')], default='Middle', max_length=255)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needs', to='apps.home')),
            ],
        ),
        migrations.AddField(
            model_name='homecategory',
            name='sale_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='apps.sale'),
        ),
    ]
