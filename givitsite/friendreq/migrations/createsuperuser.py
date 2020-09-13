import os

from django.db import migrations
from django.db.utils import IntegrityError
from django.contrib.auth.models import User

class Migration(migrations.Migration):

    dependencies = [
        ('friendreq','0004_auto_20200903_1728'),
        ('accounts', '0001_initial'), 
    ]

    def generate_superuser(apps, schema_editor):
        DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME', 'givit')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL', 'givit@example.com')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD', 'givit')

        try:
            superuser = User.objects.create_superuser(
                username=DJANGO_SU_NAME,
                email=DJANGO_SU_EMAIL,
                password=DJANGO_SU_PASSWORD)

            superuser.save()
        except IntegrityError:
            pass

    operations = [
        migrations.RunPython(generate_superuser),
    ]
