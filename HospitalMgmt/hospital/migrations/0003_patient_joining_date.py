# Generated by Django 3.2.6 on 2021-08-28 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_patient_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='joining_date',
            field=models.DateTimeField(null=True),
        ),
    ]