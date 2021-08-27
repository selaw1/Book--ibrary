from django.contrib import admin

from .models import *

admin.site.register(Book)

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [('Author Information', {'fields': ['name']})]

    inlines = [BookInline]


