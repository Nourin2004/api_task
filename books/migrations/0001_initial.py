# Generated by Django 4.1.5 on 2023-01-11 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='books/images/')),
                ('author_name', models.CharField(max_length=255)),
                ('published_date', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('star_rate', models.DecimalField(decimal_places=0, max_digits=1, max_length=5)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Books List',
                'verbose_name_plural': 'Books List',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
            ],
            options={
                'verbose_name': 'Comment List',
                'verbose_name_plural': 'Comments List',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category'),
        ),
    ]
