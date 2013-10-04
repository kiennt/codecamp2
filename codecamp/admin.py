from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from codecamp import models

class MemberAdmin(UserAdmin):
    list_filter = ('is_admin', )
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', )}),
    )
    search_fields = ('email', 'username')
    list_display = ('username', 'email', 'is_admin', 'date_joined')
    list_per_page = 50


class ChoiceInline(admin.StackedInline):
    model = models.Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]


admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.Question, QuestionAdmin)
