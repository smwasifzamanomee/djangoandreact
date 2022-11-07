from django.contrib import admin

# Register your models here.
from .models import Book,BookNumber,Character,Author

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['published']
    search_fields = ['title']
    
admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
    