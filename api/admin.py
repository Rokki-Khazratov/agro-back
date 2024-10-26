from django.contrib import admin
from django import forms
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

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'link']
    search_fields = ['name', 'category__name']





@admin.register(PlantationCategory)
class PlantationCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# Регистрируем модель District
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']
    search_fields = ['name', 'region']

# Админка для Plantation
@admin.register(Plantation)
class PlantationAdmin(admin.ModelAdmin):
    list_display = ['name', 'producer', 'garden_type', 'fruit_type', 'tree_count', 'garden_area', 'created_at']
    search_fields = ['name', 'producer', 'garden_type__name', 'district__name', 'fruit_type']
    list_filter = ['garden_type', 'district', 'fruit_type', 'created_at']
    list_editable = ['garden_type', 'fruit_type', 'tree_count']
    fieldsets = (
        ('Общая информация', {
            'fields': ('name', 'INN', 'producer', 'district', 'address', 'latitude', 'longitude')
        }),
        ('Информация о саде', {
            'fields': ('garden_type', 'category', 'fruit_type', 'planting_scheme', 'tree_count', 'garden_area', 'irrigation_type', 'productivity')
        }),
        ('Дополнительная информация', {
            'fields': ('status',)
        }),
    )
    autocomplete_fields = ['garden_type', 'category', 'district']
    readonly_fields = ['created_at']






# class PlantationForm(forms.ModelForm):
#     class Meta:
#         model = Plantation
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance and self.instance.pk:
#             # Заполняем районы в зависимости от региона, если запись существует
#             self.fields['district'].choices = self.instance.get_district_choices()

#         else:
#             # Если запись новая, скрываем список районов до выбора региона
#             self.fields['district'].choices = []

# @admin.register(Plantation)
# class PlantationAdmin(admin.ModelAdmin):
#     form = PlantationForm

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