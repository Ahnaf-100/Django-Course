from django.contrib import admin
from . import models
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']


# from django.utils.text import slugify
# from django.utils.timezone import now

# class CarAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not obj.slug:
#             obj.slug = slugify(obj.name) + '-' + now().strftime('%Y%m%d%H%M%S')
#         super().save_model(request, obj, form, change)




admin.site.register(models.Brand, CarAdmin)
admin.site.register(models.Car)
admin.site.register(models.Comment)

