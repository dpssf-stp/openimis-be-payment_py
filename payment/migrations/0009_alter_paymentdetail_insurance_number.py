# Generated by Django 4.2.10 on 2024-08-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0008_payment_serial_fix"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentdetail",
            name="insurance_number",
            field=models.CharField(
                blank=True, db_column="InsuranceNumber", max_length=50, null=True
            ),
        ),
    ]