from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links = ('first_name','last_name','username')
    #search is enabled by default
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',) # '-' it shows date in desending order

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  #it will make password readonly



admin.site.register(Account,AccountAdmin)
