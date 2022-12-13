from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Fee)
admin.site.register(FAQ)