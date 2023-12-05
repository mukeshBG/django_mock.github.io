from django.contrib import admin
from library.models import Book_management,Patron_management,Borrowing
# Register your models here.
admin.site.register(Book_management)
admin.site.register(Patron_management)
admin.site.register(Borrowing)