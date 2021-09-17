"""User admin clases"""

#Django
from django.contrib import admin # me permite importar todo el modulo admin y poder ingresar al admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from .models import Profile
from django.contrib.auth.models import User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk', 'user', 'biography','location', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('biography', 'picture')
    
    search_fields = (
        'user__email',
        'user__username'
        'user__first_name', 
        'user__last_name', 
        'locaion'
    )

    list_filter = (
        'created', 
        'user__is_active',
        'user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user' , 'picture'),
            ),
        } ),
        ('Extra info', {
            'fields': (
                ('location'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created'),),
        })
    )
    readonly_fields = ('created',)

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users"""
        
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
       
#re register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)