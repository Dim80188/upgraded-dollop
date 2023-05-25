# Generated by Django 4.2.1 on 2023-05-22 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('calories', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proteins', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carbons', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamin_a', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b1', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b2', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b4', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b5', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b6', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b9', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b12', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_c', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_d', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_e', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_h', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_k', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_pp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('potassium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calcium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('magnesium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('phosphorus', models.DecimalField(decimal_places=2, max_digits=5)),
                ('iron', models.DecimalField(decimal_places=2, max_digits=5)),
                ('iodine', models.DecimalField(decimal_places=2, max_digits=5)),
                ('manganese', models.DecimalField(decimal_places=3, max_digits=6)),
                ('copper', models.DecimalField(decimal_places=2, max_digits=5)),
                ('selenium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fluorine', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chromium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('zinc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('arginine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('valine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('histidine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('isoleucine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('leucine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('lysine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('methionine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('threonine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('tryptophan', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('phenylalanine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('alanine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('aspartic_acid', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('hydroxyproline', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('glycine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('glutamic_acid', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('proline', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('serene', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('tyrosine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('cysteine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='food.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('calories', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proteins', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carbons', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamin_a', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b1', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b2', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b4', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b5', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b6', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b9', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_b12', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_c', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_d', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_e', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_h', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_k', models.DecimalField(decimal_places=3, max_digits=6)),
                ('vitamin_pp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('potassium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calcium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('magnesium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('phosphorus', models.DecimalField(decimal_places=2, max_digits=5)),
                ('iron', models.DecimalField(decimal_places=2, max_digits=5)),
                ('iodine', models.DecimalField(decimal_places=2, max_digits=5)),
                ('manganese', models.DecimalField(decimal_places=3, max_digits=6)),
                ('copper', models.DecimalField(decimal_places=2, max_digits=5)),
                ('selenium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fluorine', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chromium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('zinc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('arginine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('valine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('histidine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('isoleucine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('leucine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('lysine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('methionine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('threonine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('tryptophan', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('phenylalanine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('alanine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('aspartic_acid', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('hydroxyproline', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('glycine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('glutamic_acid', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('proline', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('serene', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('tyrosine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('cysteine', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('event_time', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]