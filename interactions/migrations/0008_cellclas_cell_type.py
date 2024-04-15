# Generated by Django 4.0.2 on 2022-08-18 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0007_pathway_interaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellclas',
            name='cell_type',
            field=models.CharField(choices=[('n', 'Non-hematopoietic'), ('i', 'Blood & Immune Cells'), ('p', 'HPC')], default='n', max_length=1),
        ),
    ]