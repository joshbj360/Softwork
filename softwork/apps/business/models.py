from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.fields import NullBooleanField
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _

from softwork.apps.authme.models import User

class ServiceTag(models.Model):
    tag = models.SlugField()
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag
    
class Service(models.Model):
    # One cannot delete the business profile except the Business owner is deleted
    service_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(_("Price starting at:"), default=0)
    price_negotiable = models.BooleanField(_("Price is Negotiable?"), default=False)
    years_of_experience = models.IntegerField(_("Select you years of experience on the job"))
    tags = GenericRelation(ServiceTag)
    
    business_services = GenericRelation(
        'BusinessService',
        'service_object_id',
        'service_content_type_id',
        related_query_name='services',
    )
    
    def __str__(self):
        return self.service_name

       
class BusinessAddress(models.Model):
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    LGA = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    building_number = models.IntegerField(blank=True, null=True)
    address = models.TextField(_("Full Address"))
    
    business_gps_coordinates = models.FloatField(_("Find the exact business location"))
    business_is_verified = models.BooleanField(default=False)
    
    def get_full_address(self):
        return "No. {0} {1} {2} {3} State".format(self.building_number, self.street, self.LGA, self.state)
        
class BusinessProfile(BusinessAddress):
    owner = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
    )
    business_name = models.CharField(max_length=255, )
    business_motto = models.CharField(max_length=255)
    business_description = models.TextField(blank=True, null=True)
    business_logo = models.ImageField(blank=True, null=True)
    business_header_image = models.ImageField(blank=True, null=True)
    business_industry_tags = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ['business_name']
    
    def __str__(self):
        return self.business_name
    
    def add_business_service(self, service) -> 'BusinessService':
        service_content_type = ContentType.objects.get_for_model(service)
        
        return BusinessService.objects.create(
            business=self,
            service_content_type=service_content_type,
            service_object_id=service.pk,
        )

class BusinessService(models.Model):
    business = models.ForeignKey(
        BusinessProfile,
        verbose_name=_("Name of Business"),
        on_delete=models.CASCADE,
        related_name='services',
    )
    service_object_id = models.IntegerField()
    service_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
    )
    service = GenericForeignKey(
        'service_content_type',
        'service_object_id',
    )

    def __str__(self):
        return self.service.service_name
