from django.contrib import admin
from books.models import Comments, Books, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'book_name']


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Books, BooksAdmin)