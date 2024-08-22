from django.db import migrations

def create_default_poll(apps, schema_editor):
    Poll = apps.get_model('mainApp', 'Poll')
    Option = apps.get_model('mainApp', 'Option')

    default_poll, created = Poll.objects.get_or_create(question="I wish there was...")

    if created:
        Option.objects.create(poll=default_poll, option_text="Default Option")



class Migration(migrations.Migration):
    dependencies = [
        ('mainApp', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(create_default_poll),
    ]
