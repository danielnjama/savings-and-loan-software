# Generated by Django 4.2.7 on 2023-12-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contribution_amount_alter_loan_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrecord',
            name='date_paid',
            field=models.DateField(auto_now_add=True),
        ),
    ]
