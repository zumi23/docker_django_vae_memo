from django.contrib import admin

# Register your models here.
from .models import (
    Nets, GenImgs, NetFigs, HomeContents, 
)


admin.site.register(
    [Nets, GenImgs, NetFigs, HomeContents,]
)