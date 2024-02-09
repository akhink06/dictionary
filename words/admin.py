from django.contrib import admin
from words.models import Author , Word


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","user")

admin.site.register(Author)


admin.site.register(Word)