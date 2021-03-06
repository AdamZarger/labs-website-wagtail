# Generated by Django 2.0.5 on 2018-05-04 23:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('events', '0005_auto_20180428_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='keynotes',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
