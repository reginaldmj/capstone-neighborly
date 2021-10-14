from django.contrib import admin
from neighborlyUsers.models import NeighborlyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from neighborlyUsers.forms import NeighborlyUserCreationForm, NeighborlyUserChangeForm

# Register your models here.

class NeighborlyUserAdmin(UserAdmin):
    add_form = NeighborlyUserCreationForm
    form = NeighborlyUserChangeForm
    model = NeighborlyUser
    list_display = ['username', 'display_name', 'email' ]
    list_filter = ('is_staff', 'is_active', 'username')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'display_name', 'email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2', 'is_staff', 'is_active', 'username', 'display_name', 'email')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(NeighborlyUser, NeighborlyUserAdmin)