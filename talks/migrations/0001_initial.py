# Generated by Django 2.0.4 on 2018-04-28 16:56

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('hero', wagtail.core.fields.StreamField((('hero', wagtail.core.blocks.StructBlock((('subject', wagtail.core.blocks.CharBlock()), ('byline', wagtail.core.blocks.CharBlock(required=False))))),))),
                ('author', wagtail.core.fields.RichTextField()),
                ('body', wagtail.core.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
