# Generated by Django 2.0.4 on 2018-04-28 18:28

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='talk',
            name='hero',
            field=wagtail.core.fields.StreamField((('hero', wagtail.core.blocks.StructBlock((('subject', wagtail.core.blocks.CharBlock(required=False)),))),)),
        ),
    ]
