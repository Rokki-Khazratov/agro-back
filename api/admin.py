from django.contrib import admin
from .models import *

# Inline admin for images
class NewsImageAdmin(admin.StackedInline):
    model = NewsImage
    extra = 1  # Number of empty fields to show for adding images

# Main admin for News with inline images
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin]  # Embed NewsImage admin
    list_display = ['title', 'category', 'created_at', 'updated_at']
    search_fields = ['title', 'category']
    list_filter = ['category', 'created_at']

@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')


@admin.register(Plantation)
class PlantationAdmin(admin.ModelAdmin):
    list_display = ('producer', 'latitude','longitude', 'status', 'area_size', 'crop_type', 'established_date')
    search_fields = ('producer__first_name', 'producer__last_name', 'crop_type')
    list_filter = ('status', 'crop_type')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'link']
    search_fields = ['name', 'category__name']



# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'message', 'is_read', 'created_at')
#     search_fields = ('user__email', 'message')
#     list_filter = ('is_read', 'created_at')

# @admin.register(PasswordResetToken)
# class PasswordResetTokenAdmin(admin.ModelAdmin):
#     list_display = ('user', 'token', 'expires_at', 'created_at')
#     search_fields = ('user__email', 'token')
#     list_filter = ('expires_at',)


admin.site.register(NewsCategory)