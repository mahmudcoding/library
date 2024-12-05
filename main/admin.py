from django.contrib import admin
from .models import Book, Person

# Book Admin Configuration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isAvailable', 'isBorrowed', 'isReserved', 'place_number')
    search_fields = ('title', 'author')
    list_filter = ('isAvailable', 'isBorrowed', 'isReserved')
    ordering = ('id',)

# Person Admin Configuration
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'login', 'role')
    search_fields = ('name', 'login', 'role')
    list_filter = ('role',)
    ordering = ('id',)
