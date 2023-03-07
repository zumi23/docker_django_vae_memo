# Django のデータベースにデータの追加を可能にする設定
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from django import setup
setup()

import csv
from vaes.models import (
    Nets, GenImgs, NetFigs,
)

n = Nets.objects
# print(Nets.objects.all().filter(n_z=1).count())
print(n.all().filter(rep__gte=0.8))
print(n.all().filter(rep__gte=0.8).count())
print(n.first().dr)
print(n.all()[:10])
