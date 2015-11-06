from django.contrib import admin
from models import User
from models import Question
from models import Response
from models import Tag
from models import Like


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'question', 'is_right', 'created',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('text',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'question',)


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Like, LikeAdmin)
