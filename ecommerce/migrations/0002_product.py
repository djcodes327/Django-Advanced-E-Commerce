# Generated by Django 3.1.3 on 2020-11-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', max_length=255, unique=True)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('image', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='ecommerce.Category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]