# Generated by Django 4.2.3 on 2024-01-21 19:52

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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt_response', models.CharField(max_length=400, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('stay_len', models.CharField(max_length=20, null=True)),
                ('age', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recommend.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('review_summary', models.TextField(blank=True)),
                ('website_link', models.URLField(blank=True)),
                ('image_url', models.URLField(blank=True)),
                ('price', models.CharField(max_length=200)),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itenerary', models.CharField(max_length=400, null=True)),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('recommendation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recommend.recommendation')),
            ],
        ),
    ]