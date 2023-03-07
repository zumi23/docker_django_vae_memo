from django.db import models
from accounts.models import Users
from django.urls import reverse_lazy
from django.dispatch import receiver
import os
import logging

# application_logger = logging.getLogger('application-logger')


# class BaseModel(models.Model):
#     create_at = models.DateTimeField(null=True)
#     update_at = models.DateTimeField(null=True)

#     class Meta:
#         abstract = True # 抽象モデルとして定義＞このクラスを基にモデルを作成


class Nets(models.Model):
    n_z = models.IntegerField()
    n_layer = models.IntegerField()
    n_count = models.IntegerField()
    rep = models.FloatField(null=True)
    dr = models.FloatField(null=True)
    dr_0 = models.FloatField(null=True)
    dr_1 = models.FloatField(null=True)
    dr_2 = models.FloatField(null=True)
    dr_3 = models.FloatField(null=True)
    dr_4 = models.FloatField(null=True)
    dr_5 = models.FloatField(null=True)
    dr_6 = models.FloatField(null=True)
    dr_7 = models.FloatField(null=True)
    dr_8 = models.FloatField(null=True)
    dr_9 = models.FloatField(null=True)
    id_net = models.IntegerField(null=True)

    class Meta:
        db_table = 'nets'

    def __str__(self):
        return f'{self.n_z}, {self.n_layer}, {self.n_count}'

    # def get_absolute_url(self):
    #     return reverse_lazy('vaes:detail_net', kwargs={'pk': self.pk}) # 使用例：templateからaタグ内で呼び出し、詳細画面へのリンクとして機能させる


class NetFigs(models.Model):
    rep_figpath = models.CharField(max_length=255, null=True)
    dr_figpath = models.CharField(max_length=255, null=True)
    dr_rep_figpath = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'net_figs'


class GenImgs(models.Model):
    genimgs_dir = models.CharField(max_length=255, null=True)
    net = models.OneToOneField(
        Nets,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        db_table = 'gen_imgs'


class HomeContents(models.Model):
    title = models.CharField(max_length=255, null=True)
    img_path = models.CharField(max_length=255, null=True)
    action_url = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'home_contents'