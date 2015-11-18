from django.contrib import admin
from models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'avatar')


admin.site.register(User, UserAdmin)
