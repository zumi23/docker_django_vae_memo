from django import forms
# from .models import Books, Pictures, CartItems, Addresses
from .models import (
    Nets,
)

from datetime import datetime
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.core.cache import cache


class NetImgForm(forms.ModelForm):
    model = Nets
    field = ['label',]
