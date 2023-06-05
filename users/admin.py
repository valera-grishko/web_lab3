from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group

from .models import CustomUser, Administrator, Client


admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'status', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'status')
    search_fields = ('email',)
    ordering = ('-id',)
    icon_name = 'people'
    fieldsets = (
        ('Особиста інформація',
         {'fields': (
             'email', 'first_name', 'gender', 'birth_date', 'password', 'status')}),
        ('Дозволи', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'gender', 'birth_date', 'password1', 'password2', 'is_staff',
                'is_active', 'is_superuser')}
         ),
    )


@admin.register(Client)
class ClientAdmin(CustomUserAdmin):
    icon_name = 'person'
    model = Client

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)


@admin.register(Administrator)
class AdministratorAdmin(CustomUserAdmin):
    icon_name = 'verified_user'
    model = Administrator

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=True)