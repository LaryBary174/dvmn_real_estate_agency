

from django.db import migrations
import phonenumbers

def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.iterator():
        parsed_number = phonenumbers.parse(
            flat.owners_phonenumber, "RU"
        )
        if phonenumbers.is_valid_number(parsed_number):
            flat.owner_pure_phone = parsed_number
        else:
            flat.owner_pure_phone = None

            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone_alter_flat_has_balcony'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
