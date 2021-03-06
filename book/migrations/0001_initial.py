# Generated by Django 3.1.6 on 2021-02-13 05:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('publication', models.DateField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('isbn', models.CharField(blank=True, max_length=40, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
    ]
