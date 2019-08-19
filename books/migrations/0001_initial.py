# Generated by Django 2.2.4 on 2019-08-13 15:15

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
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='booker/book_covers')),
                ('small_image', models.ImageField(blank=True, null=True, upload_to='booker/small_book_covers')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('vote', models.IntegerField(default=0)),
                ('good_id', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='VotedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voted_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookInVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('book_in_vote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
    ]