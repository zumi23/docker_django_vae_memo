from django.urls import path
from .views import (
    IndexView, PrepareView,
    NetsListView, NetDetailView, CompareImagesView, EffectsOnGenimgsView,
)
from . import views

app_name = 'vaes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('prepare/', PrepareView.as_view(), name='prepare'),
    path('nets_list/', NetsListView.as_view(), name='nets_list'),
    path('net_detail/<int:pk>', NetDetailView.as_view(), name='net_detail'),
    path('compare_images/', CompareImagesView.as_view(), name='compare_images'),
    path('effects_on_genimgs/', EffectsOnGenimgsView.as_view(), name='effects_on_genimgs'),
    path('generate_model/', PrepareView.as_view(), name='generate_model'),
    path('classify_model/', PrepareView.as_view(), name='classify_model'),
]
