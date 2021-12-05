from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin


GENDER_SELECTION = [
      ('male', 'Male'),
      ('female', 'Female'),
      ('notspecified', 'Not specified')
    ]

class User(AbstractUser, PermissionsMixin):
    """My defined user model, all other users must inherit form this model.
    :

    Args:
        AbstractBaseUser (Abstract Model): Provides the core implementation of a user model.
        PermissionsMixin (Abstract Model): [Gives us access to Django's default permission framework]
    """
    email                 = models.EmailField(help_text=_("Email address"), max_length=255, unique=True, db_index=True)
    first_name            = models.CharField(help_text=_("First Name"), max_length=50)
    last_name             = models.CharField(help_text=_("Last Name"), max_length=50)
    owner_phone_number    = models.CharField(help_text=_("Personal Moblie Number"), max_length=11, blank=True, null=True)
    NIN_number            = models.BigIntegerField(help_text=_("National Identity Number"),  blank=True, null=True)
    gender                = models.CharField(help_text=_("Select your gender"),max_length=20, choices=GENDER_SELECTION, default='notspecified')
    nationality           = models.CharField(help_text=_("Country of origin"),max_length=20, default="",blank=True)    
    soo                   = models.CharField(help_text=_("State of origin"), max_length=200, default="",blank=True)    
    lga                   = models.CharField(help_text=_("Local Govt. Area"), max_length=200, default="",blank=True)
        
    date_modified         = models.DateTimeField( auto_now=True)
    
    # objects               = UserManager()
    
    is_staff              = models.BooleanField(default=False)
    is_active             = models.BooleanField(default=True)
    is_superuser          = models.BooleanField(default=False)
    
    USERNAME_FIELD        = 'email'
    REQUIRED_FIELDS       = ['username', 'first_name']  
    
    
    class Meta:
        ordering = [ 'first_name', 'last_name']
        
    def year_joined(self):
        return self.date_joined.year() 
    
    def get_full_name(self):
        return (self.first_name+' '+self.last_name)
 
    def get_short_name(self):
        return self.first_name
 
    def natural_key(self):
        return (self.first_name, self.last_name)
 
    def __str__(self):
        return self.email