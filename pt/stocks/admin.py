from django.contrib import admin
from .models import Fabrics,Items,Makers,Partycodes,Fabnames

# Register your models here.

@admin.register(Fabrics)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','partycode','color','meter','fabric','maker','time','cutting','cut_time','item','rec_pcs','gr_pcs','completed','hsb_clr')

@admin.register(Items)
class Items(admin.ModelAdmin):
    list_display = ('id','get_maker','item','rate')

@admin.register(Makers)
class Makers(admin.ModelAdmin):
    list_display = ('id','maker')

@admin.register(Partycodes)
class Partycodes(admin.ModelAdmin):
    list_display = ('id','partycode')

@admin.register(Fabnames)
class Fabnames(admin.ModelAdmin):
    list_display = ('id','fabname')