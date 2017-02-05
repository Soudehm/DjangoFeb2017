from django.contrib import admin

# Register your models here.
from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline):
     model = Choice
     extra = 3
admin.site.register(Choice)


### fieldsets is the title of the fieldset.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']})
    ]
    inlines = [ChoiceInline]
#    list_display = ('question_text','pub_date')
    list_display = ('question_text','pub_date','was_published_recently')
    #### displays the Filter / by date published bar on the right side of admin page
    list_filter = ['pub_date']
    #### display the search
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date','question_text']




