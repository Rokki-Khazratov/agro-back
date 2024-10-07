from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'author', 'created_at')
#     search_fields = ('title', 'category')
#     list_filter = ('category', 'created_at')

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type', 'variety', 'region', 'producer', 'harvest_time')
#     search_fields = ('name', 'type', 'variety')
#     list_filter = ('region', 'harvest_time')

# @admin.register(Plantation)
# class PlantationAdmin(admin.ModelAdmin):
#     list_display = ('producer', 'location', 'status', 'area_size', 'crop_type', 'established_date')
#     search_fields = ('producer__first_name', 'producer__last_name', 'crop_type')
#     list_filter = ('status', 'crop_type')

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