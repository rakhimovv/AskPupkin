from django.contrib import admin
from models import Question
from models import Response


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date')


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'question', 'is_right', 'creation_date',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Response, ResponseAdmin)
