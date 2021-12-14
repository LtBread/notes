from os.path import join
import json
from django.core.management.base import BaseCommand

from users.models import User

# python manage.py dumpdata users.User > users/fixtures/users.json
# python manage.py loaddata users/fixtures/users.json

JSON_PATH = 'users/fixtures'


def load_from_json(file_name):
    with open(join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('users')

        User.objects.all().delete()
        for user in users:
            new_user = User(**user)
            new_user.save()

        super_user = User.objects.create_superuser('admin', 'admin@notes.local', 'admin')
