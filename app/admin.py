from django.contrib import admin

from .models import *

admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(User)
admin.site.register(Borrow)