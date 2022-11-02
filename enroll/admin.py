from django.contrib import admin

from .models import User 


#### register User model to make datatables and to display fields in admin page in django

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']