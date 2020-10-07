from django.contrib import admin

from .forms import *


class AccountAdmin(admin.ModelAdmin):
    form = AccountForm


# Register your models here.
admin.site.register(Flashcard)
admin.site.register(Lesson)
admin.site.register(Account, AccountAdmin)
admin.site.register(Course)
