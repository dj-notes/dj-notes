# Generated by Django 3.2.13 on 2022-06-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notebook'),
        ('books', '0002_alter_notebook_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='notes',
        ),
        migrations.AddField(
            model_name='notebook',
            name='notes',
            field=models.ManyToManyField(blank=True, null=True, related_name='booknotes', to='notes.Note'),
        ),
    ]
