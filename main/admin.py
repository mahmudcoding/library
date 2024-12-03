from django.contrib import admin
from .models import Book, Person, Library

# Book Admin Configuration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isAvailable', 'isBorrowed', 'isReserved', 'library_id', 'place_number')
    search_fields = ('title', 'author')
    list_filter = ('isAvailable', 'isBorrowed', 'isReserved')
    ordering = ('id',)

# Person Admin Configuration
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'login', 'role', 'library_id')
    search_fields = ('name', 'login', 'role')
    list_filter = ('role',)
    ordering = ('id',)

# Library Admin Configuration
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name', 'location')
    ordering = ('id',)
