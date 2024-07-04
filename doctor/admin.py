from django.contrib import admin
from .models import Designation,Specialization,AvailableTime,Doctor,Review
# Register your models here.
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Designation, DesignationAdmin)
class SpecalizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Specialization, SpecalizationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)
