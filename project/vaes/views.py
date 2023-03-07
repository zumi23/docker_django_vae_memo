from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import (
    View, TemplateView, RedirectView,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
    FormView,
)

from .models import(
    Nets, GenImgs, HomeContents, 
    # Books, Pictures,
    # Products, Carts, CartItems, Addresses,
    # Orders, OrderItems,
)
    
# from . import forms
# from .forms import(
#     # CartUpdateForm, AddressInputForm,
# )

import os
from datetime import datetime
from django.urls import reverse_lazy
import logging, csv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse, Http404
from django.core.cache import cache
from django.db import transaction

# application_logger = logging.getLogger('application-logger') # 引数にはsettings.py内のloggerの設定で定義したロガー名を用いる
# error_logger = logging.getLogger('error-logger')

class IndexView(ListView):
    model = HomeContents
    template_name = os.path.join('vaes', 'index.html')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # # application_logger.debug('Home画面を表示します')
        # # Http404のログを取得するテスト
        # if kwargs.get('name') == 'aaaa':
        #     # error_logger.error('この名前は使用できません') middleware.py内に記述
        #     raise Http404('この名前は使用できません')
        # # templateに渡す値を記述
        # context['name'] = kwargs.get('name')
        # context['time'] = datetime.now()
        return context
    
    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        qs = qs.order_by('id')
        return qs

class PrepareView(TemplateView):
    template_name = os.path.join('vaes', 'prepare.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NetsListView(ListView):
    model = Nets
    template_name = os.path.join('vaes', 'list_nets.html')
    # paginate_by = 15

    def get_queryset(self):
        qs = super(NetsListView, self).get_queryset()
        tmp_z = self.request.GET.get('tmp_z', '-')
        tmp_layer = self.request.GET.get('tmp_layer', '-')
        tmp_count = self.request.GET.get('tmp_count', '-')
        tmp_order_col = self.request.GET.get('tmp_order_col', 'id_net')
        tmp_order_method  = self.request.GET.get('tmp_order_method', '1')
        print(f'{tmp_z}, {tmp_layer}, {tmp_count}, {tmp_order_col}')
        if tmp_z != '-':
            qs = qs.filter(n_z=tmp_z)
        if tmp_layer != '-':
            qs = qs.filter(n_layer=tmp_layer)
        if tmp_count != '-':
            qs = qs.filter(n_count=tmp_count)
        # print(qs)
        if tmp_order_method == '1':
            qs = qs.order_by(tmp_order_col)
        elif tmp_order_method == '2':
            qs = qs.order_by('-' + tmp_order_col)
        return qs


        # qs = qs.order_by('-id')
        # qs = qs.filter(name__startswith='book')
        # if 'name' in self.kwargs:
        #     qs = qs.filter(name__startswith=self.kwargs['name'])
        # qs = qs.order_by('n_z')
        # return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        # context['form'] = forms.BookForm()
        tmp_ary_1 = [2**x for x in range(5)]
        tmp_ary_1.insert(0, '-')
        tmp_ary_2 = [2**(x+1)-1 for x in range(3)]
        tmp_ary_2.insert(0, '-')
        tmp_ary_3 = [x+1 for x in range(5)]
        tmp_ary_3.insert(0, '-')
        tmp_ary_4 = ['id_net', 'rep', 'dr']
        context['option_z_ary'] = tmp_ary_1
        context['option_layer_ary'] = tmp_ary_2
        context['option_count_ary'] = tmp_ary_3
        context['option_order_col_ary'] = tmp_ary_4

        # genimg_all = f'{self.object.genimgs.genimgs_dir}/all.png'
        # context['genimg_all'] = genimg_all

        # フォーム入力内容を保存
        context['tmp_z'] = self.request.GET.get('tmp_z', '')
        context['tmp_layer'] = self.request.GET.get('tmp_layer', '')
        context['tmp_count'] = self.request.GET.get('tmp_count', '')

        context['tmp_order_col'] = self.request.GET.get('tmp_order_col', 'id_net')
        tmp_order_method = self.request.GET.get('tmp_order_method', '1')
        if tmp_order_method == '1':
            context['ascending'] = True
            context['tmp_order_method_name'] = 'ascending'
        elif tmp_order_method == '2':
            context['descending'] = True
            context['tmp_order_method_name'] = 'descending'
        return context

        # realimg_n = f'/static/img/vaes/real/{tmp_label}.png'
        # genimg_n = f'{self.object.genimgs.genimgs_dir}/{tmp_label}.png'
        # context['realimg_n'] = realimg_n
        # context['genimg_n'] = genimg_n
        # context['test'] = self.object.genimgs.genimgs_dir
                
        return context
    

class NetDetailView(DetailView):
    # 詳細を表示するモデルを指定
    model = Nets
    template_name = os.path.join('vaes', 'net_detail.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        # context['form'] = forms.BookForm()
        context['option_ary'] = [int(x) for x in range(10)]

        genimg_all = f'{self.object.genimgs.genimgs_dir}/all.png'
        context['genimg_all'] = genimg_all

        tmp_label = self.request.GET.get('label_n', 0)
        realimg_n = f'/static/img/vaes/real/{tmp_label}.png'
        genimg_n = f'{self.object.genimgs.genimgs_dir}/{tmp_label}.png'
        context['realimg_n'] = realimg_n
        context['genimg_n'] = genimg_n
        context['label_n'] = tmp_label
        # context['test'] = self.object.genimgs.genimgs_dir
        
        
        return context
    

class CompareImagesView(ListView):
    # 詳細を表示するモデルを指定
    model = Nets
    template_name = os.path.join('vaes', 'compare_images.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['option_label_ary'] = [int(x) for x in range(10)]
        option_z_ary = [2**x for x in range(5)]
        # option_z_ary.insert(0, '-')
        option_layer_ary = [2**(x+1)-1 for x in range(3)]
        # option_layer_ary.insert(0, '-')
        option_count_ary = [x+1 for x in range(5)]
        option_count_ary.append('real')
        context['option_z_ary'] = option_z_ary
        context['option_layer_ary'] = option_layer_ary
        context['option_count_ary'] = option_count_ary

        obj_ary = [[], [], []]

        label_n = self.request.GET.get('label_n', 0)
        net_info_a = [self.request.GET.get('n_z_a', 1), self.request.GET.get('n_layer_a', 1), self.request.GET.get('n_count_a', 'real')]
        net_info_b = [self.request.GET.get('n_z_b', 1), self.request.GET.get('n_layer_b', 1), self.request.GET.get('n_count_b', 'real')]
        net_info_c = [self.request.GET.get('n_z_c', 1), self.request.GET.get('n_layer_c', 1), self.request.GET.get('n_count_c', 'real')]

        if net_info_a[2] != 'real':
            obj_a = Nets.objects.filter(n_z=net_info_a[0], n_layer=net_info_a[1], n_count=net_info_a[2]).first()
            obj_ary[0].append(obj_a)
            genimg_a = f'{obj_a.genimgs.genimgs_dir}/{label_n}.png'
        else:
            for i in range(5):
                obj_a = Nets.objects.filter(n_z=net_info_a[0], n_layer=net_info_a[1], n_count=i+1).first()
                obj_ary[0].append(obj_a)
            genimg_a = f'/static/img/vaes/real/{label_n}.png'
        
        if net_info_b[2] != 'real':
            obj_b = Nets.objects.filter(n_z=net_info_b[0], n_layer=net_info_b[1], n_count=net_info_b[2]).first()
            obj_ary[1].append(obj_b)
            genimg_b = f'{obj_b.genimgs.genimgs_dir}/{label_n}.png'
        else:
            for i in range(5):
                obj_b = Nets.objects.filter(n_z=net_info_b[0], n_layer=net_info_b[1], n_count=i+1).first()
                obj_ary[1].append(obj_b)
            genimg_b = f'/static/img/vaes/real/{label_n}.png'

        if net_info_c[2] != 'real':
            obj_c = Nets.objects.filter(n_z=net_info_c[0], n_layer=net_info_c[1], n_count=net_info_c[2]).first()
            obj_ary[2].append(obj_c)
            genimg_c = f'{obj_c.genimgs.genimgs_dir}/{label_n}.png'
        else:
            for i in range(5):
                obj_c = Nets.objects.filter(n_z=net_info_c[0], n_layer=net_info_c[1], n_count=i+1).first()
                obj_ary[2].append(obj_c)
            genimg_c = f'/static/img/vaes/real/{label_n}.png'

        context['label_n'] = label_n
        context['obj_ary'] = obj_ary

        context['net_info_a'] = net_info_a
        context['genimg_a'] = genimg_a

        context['net_info_b'] = net_info_b
        context['genimg_b'] = genimg_b

        context['net_info_c'] = net_info_c
        context['genimg_c'] = genimg_c

        context['dr_rep'] = '/static/img/vaes/dr_rep.png'
        return context
    
    def get_queryset(self):
        qs= super(CompareImagesView, self).get_queryset()
        
        # qs = qs.order_by('n_count')
        return qs
