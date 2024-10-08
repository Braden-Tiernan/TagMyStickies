# Generated by Django 4.2.15 on 2024-09-05 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserEntry',
            fields=[
                ('user', models.IntegerField(primary_key=True, serialize=False)),
                ('chat', models.IntegerField(unique=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='StickerTagEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sticker', models.CharField(max_length=128)),
                ('tag', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stickers', to='records.userentry')),
            ],
            options={
                'ordering': ['sticker'],
            },
        ),
    ]
