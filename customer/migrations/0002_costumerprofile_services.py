# Generated by Django 4.1.4 on 2022-12-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumerprofile',
            name='services',
            field=models.CharField(blank=True, choices=[('Weight Management', 'Weight Management'), ('Sports Nutrition', 'Sports Nutrition'), ('Kids Nutrition', 'Kids Nutrition'), ('Fitness Nutrition', 'Fitness Nutrition')], max_length=100, null=True),
        ),
    ]
