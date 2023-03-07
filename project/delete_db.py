# Django のデータベースにデータの追加を可能にする設定
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from django import setup
setup()

import csv
from vaes.models import (
    Nets, GenImgs, NetFigs, HomeContents,
)

Nets.objects.all().delete()
GenImgs.objects.all().delete()
NetFigs.objects.all().delete()
HomeContents.objects.all().delete()

print("completed delete db")