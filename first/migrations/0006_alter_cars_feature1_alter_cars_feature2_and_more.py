# Generated by Django 4.2.7 on 2023-12-28 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_rename_fueltank_cars_feature1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='feature1',
            field=models.CharField(blank=True, default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cars',
            name='feature2',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='feature3',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='feature4',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='feature5',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='feature6',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='feature7',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='feature8',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='feature9',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
