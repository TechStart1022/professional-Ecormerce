from django.contrib import admin
from userauths.models import User,Profile



class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','phone']
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name','gender','country']
    list_editable = ['gender','country']

admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)



# Register your models here.
