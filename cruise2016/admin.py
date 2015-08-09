from django.contrib import admin

from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):

    list_display = ('name', 'host_name', 'signup_date', 'paid')

admin.site.register(SignUp, SignUpAdmin)