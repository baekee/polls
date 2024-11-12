from symtable import Class

from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    inlines = [ChoiceInline]

    list_filter = ['pub_date', 'was_published_recently']
    search_fields = ['question_text']

# Register your models here.
# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)