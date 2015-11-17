from django.contrib import admin
from models import Tag
from models import Like


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'question',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Like, LikeAdmin)
