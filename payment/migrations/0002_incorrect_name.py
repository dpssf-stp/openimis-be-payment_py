# Generated by Django 3.0.3 on 2021-01-26 10:44
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
IF (EXISTS (SELECT * 
         FROM INFORMATION_SCHEMA.TABLES 
         WHERE TABLE_SCHEMA = SCHEMA_NAME() 
         AND  TABLE_NAME = 'contribution_PaymentMutation'))
BEGIN
exec sp_rename 'contribution_PaymentMutation', 'payment_PaymentMutation', 'OBJECT'
END
            """
            if "sql_server" in settings.DB_ENGINE else
            """
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'contribution_PaymentMutation') THEN  
        EXECUTE 'ALTER TABLE "contribution_PaymentMutation" RENAME TO "payment_PaymentMutation"';
    END IF;
END$$;            
            """
                          )
    ]
