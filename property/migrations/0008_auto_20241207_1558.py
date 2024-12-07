

from django.db import migrations
import phonenumbers

def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')  # Замените myapp на имя вашего приложения

    for flat in Flat.objects.all():
        flat.owner_pure_phone = phonenumbers.parse(
            flat.owners_phonenumber, "RU"
        )
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone_alter_flat_has_balcony'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
