# Generated by Django 2.0.5 on 2018-05-11 13:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0004_talklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='description',
        ),
        migrations.AddField(
            model_name='talk',
            name='exerpt',
            field=wagtail.core.fields.RichTextField(default='', help_text='Summary for list view, not displayed in detail view'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='talk',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()))),
        ),
    ]