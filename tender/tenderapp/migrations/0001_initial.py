# Generated by Django 3.0.3 on 2020-06-22 13:48

from django.db import migrations, models
import tenderapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('org_name', models.CharField(blank=True, max_length=50, null=True)),
                ('org_add', models.CharField(blank=True, max_length=50, null=True)),
                ('service', models.CharField(blank=True, max_length=50, null=True)),
                ('tender_description', models.TextField()),
                ('published_on', models.DateTimeField()),
                ('published_date', models.DateTimeField()),
                ('last_date', models.DateTimeField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to=tenderapp.models.upload_location)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('tender_type', models.CharField(choices=[('Tender', 'tender'), ('Quotation', 'quotation'), ('Proposal', 'proposal'), ('EOI', 'eoi'), ('StandingList', 'standinglist'), ('Auction', 'auction'), ('IntentToAward', 'intenttoaward')], default='Tender', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
