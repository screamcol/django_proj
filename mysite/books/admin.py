from django.contrib import admin
from books.models import Publisher, Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date', 'publisher')
    search_fields = ('title',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title', 'authors', 'publisher')
    filter_horizontal = ('authors',)
    #raw_id_fields = ('publisher',)
		

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)