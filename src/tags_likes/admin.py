from django.contrib import admin
from models import Tag
from models import QuestionLike
from models import ResponseLike


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


class QuestionLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'question',)


class ResponseLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'response',)


admin.site.register(Tag, TagAdmin)
admin.site.register(QuestionLike, QuestionLikeAdmin)
admin.site.register(ResponseLike, ResponseLikeAdmin)
