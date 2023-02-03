import json
from datetime import datetime

from django.db import migrations


def load_from_json():
    with open(r'F:\moduls\modul-10\notes\noteapp\migrations\author.json', encoding="utf-8") as f:
        data = json.load(f)
        return data


def fill_authors(apps, schema_editor):
    author = apps.get_model("noteapp", "Author")
    data = load_from_json()
    for auth in data:
        author.objects.create(full_name=auth["fullname"],
                              born_date=datetime.strptime(auth["born_date"], "%B %d, %Y"),
                              born_location=auth["born_location"],
                              description=auth["description"],
                              )


class Migration(migrations.Migration):
    dependencies = [
        ('noteapp', '0005_auto_20230203_2153'),
    ]

    operations = [
        migrations.RunPython(fill_authors)
    ]
