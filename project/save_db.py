# Django のデータベースにデータの追加を可能にする設定
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from django import setup
setup()

import csv
from vaes.models import (
    Nets, GenImgs, NetFigs, HomeContents,
)
from datetime import datetime


save_file_tpl = '{}_{}.csv'

dt = datetime.now()
date_tpl = '{:04}{:02}{:02}_{:02}{:02}{:02}'
tmp_date = date_tpl.format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
# print(tmp_date)

tmp_name = 'vae_data' # change here
save_file = save_file_tpl.format(tmp_name, tmp_date)
# print(save_file)

save_file_path = os.path.join('static', 'db', 'vaes', 'logs', save_file)
# print(save_file_path)

with open(save_file_path, "w") as output_file:
    f = csv.writer(output_file)
    qs = Nets.objects.all()
    for qs_i in qs:
        f.writerow([qs_i.n_z, qs_i.n_layer, qs_i.n_count, qs_i.dr_0, qs_i.dr_1, qs_i.dr_2, qs_i.dr_3, qs_i.dr_4, qs_i.dr_5, qs_i.dr_6, qs_i.dr_7, qs_i.dr_8, qs_i.dr_9, qs_i.dr, qs_i.rep])


tmp_name = 'home_contents' # change here
save_file = save_file_tpl.format(tmp_name, tmp_date)
# print(save_file)

save_file_path = os.path.join('static', 'db', 'vaes', 'logs', save_file)
# print(save_file_path)

with open(save_file_path, "w") as output_file:
    f = csv.writer(output_file)
    qs = HomeContents.objects.all()
    for qs_i in qs:
        f.writerow([qs_i.title, qs_i.action])


print("completed saving db")