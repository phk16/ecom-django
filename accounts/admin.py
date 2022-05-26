from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    #to make password immutable
    list_display=('email', 'first_name', 'last_name', 'last_login', 'is_active', 'date_joined')
    #to make fields as links
    list_display_links=('email', 'first_name', 'last_name')
    #to make read-only
    readonly_fields=('last_login', 'date_joined')
    #order by date joined
    ordering=('date_joined',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Account, AccountAdmin)