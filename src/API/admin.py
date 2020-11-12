from django.contrib import admin


from .models import Poll, Question, Choice, Answer


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'end_date')
    list_filter = ('name', 'end_date')
    readonly_fields = ('begin_date',)
    fieldsets = (
        (None, {
            "fields": ("name",)
        }),
        (None, {
            "fields": ("description",)
        }),
        (None, {
            "fields": (("begin_date", "end_date"),)
        }),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('poll', 'description')
    list_filter = ('poll__name', )
    search_fields = ('poll__name', )
    fieldsets = (
        (None, {
            "fields": ("poll",)
        }),
        (None, {
            "fields": ("description",)
        }),
        (None, {
            "fields": ("type",)
        }),
    )


admin.site.register(Choice)
