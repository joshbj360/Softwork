from django.contrib import admin

from .models import BusinessProfile, ServiceTag, Service, BusinessService


admin.site.register(BusinessProfile)
admin.site.register(ServiceTag)
admin.site.register(Service)
admin.site.register(BusinessService)