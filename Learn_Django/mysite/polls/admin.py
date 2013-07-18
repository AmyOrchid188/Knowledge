from django.contrib import admin
from polls.models import Choice, Poll

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
# Register your models here.
# admin.site.register(Poll)
class PollAdmin(admin.ModelAdmin):
    # fields=['pub_date', 'questions']
#    fieldsets = [
#        (None,              {'fields': ['questions']}),
#        ('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}),
#        ]
#
#
#    inlines = [ChoiceInline]
    search_fields = ['questions']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    list_display = ('questions', 'pub_date', 'was_published_recently')
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
