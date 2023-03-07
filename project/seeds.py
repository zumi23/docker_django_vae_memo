# Django のデータベースにデータの追加を可能にする設定
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from django import setup
setup()

import csv
from vaes.models import (
    Nets, GenImgs, NetFigs, HomeContents,
)
from django.urls import reverse_lazy


file_path = os.path.join('static', 'db', 'vaes', 'vae_data.csv')
id_net_tpl = "{:02}{:02}{:02}"

with open(file_path, "r") as input_file:
    f = csv.reader(input_file)

    for row_i in f:
        n = Nets(
            n_z = int(row_i[0]),
            n_layer = int(row_i[1]),
            n_count = int(row_i[2]),
            rep = float(row_i[14]),
            dr = float(row_i[13]),
            dr_0 = float(row_i[3]),
            dr_1 = float(row_i[4]),
            dr_2 = float(row_i[5]),
            dr_3 = float(row_i[6]),
            dr_4 = float(row_i[7]),
            dr_5 = float(row_i[8]),
            dr_6 = float(row_i[9]),
            dr_7 = float(row_i[10]),
            dr_8 = float(row_i[11]),
            dr_9 = float(row_i[12]),
            id_net = int(id_net_tpl.format(int(row_i[0]), int(row_i[1]), int(row_i[2])))
        )
        n.save()

        tmp_dir = os.path.join('/static', 'img', 'vaes', f'z{n.n_z}', f'l{n.n_layer}', f'c{n.n_count}')
        g = GenImgs(
            genimgs_dir = tmp_dir,
            net = n,
        )
        g.save()


file_path = os.path.join('static', 'db', 'vaes', 'home_contents.csv')
img_path_tpl = "/static/img/vaes/home_contents_imgs/{}.png"
action_url_tpl = "vaes:{}"

with open(file_path, "r") as input_file:
    f = csv.reader(input_file)
    for row_i in f:
        n = HomeContents.objects.create(
            title = str(row_i[0]),
            img_path = img_path_tpl.format(row_i[1]),
            action_url = reverse_lazy(action_url_tpl.format(row_i[1])),
        )
        n.save()

print("completed reading csv")

