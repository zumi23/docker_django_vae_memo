from django.urls import path
from .views import (
    IndexView, PrepareView,
    NetsListView, NetDetailView, CompareImagesView, 
)
from . import views

app_name = 'vaes'

urlpatterns = [
    # path('item_list/', views.item_list, name='item_list'),
    # path('item_detail/<int:id>', views.item_detail, name='item_detail'),
    # path('to_google/', views.to_google, name='to_google'),
    # path('one_item/', views.one_item, name='one_item'),
    path('', IndexView.as_view(), name='index'),
    path('prepare/', PrepareView.as_view(), name='prepare'),
    path('nets_list/', NetsListView.as_view(), name='nets_list'),
    path('net_detail/<int:pk>', NetDetailView.as_view(), name='net_detail'),
    path('compare_images/', CompareImagesView.as_view(), name='compare_images'),
    path('effects_on_genimg/', CompareImagesView.as_view(), name='effects_on_genimg'),
    path('generate_model/', PrepareView.as_view(), name='generate_model'),
    path('classify_model/', PrepareView.as_view(), name='classify_model'),
]
