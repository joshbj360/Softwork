from django.db import transaction

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import GENDER_SELECTION, User

# class UserSerializer(RegisterSerializer):
    
#     first_name            = serializers.CharField(max_length=50)
#     last_name             = serializers.CharField( max_length=50)
#     gender                = serializers.ChoiceField(choices=GENDER_SELECTION, default='notspecified')
#     nationality           = serializers.CharField(max_length=20, default="")    
#     soo                   = serializers.CharField(max_length=200, default="")    
#     lga                   = serializers.CharField(max_length=200, default="")

#     # Define transaction.atomic to rollback the save operation of error
#     @transaction.atomic
#     def save(self, request):
#         user = super().save(request)
#         user.first_name = self.data.get('first_name')
#         user.last_name = self.data.get('last_name')
#         user.gender = self.data.get('gender')
#         user.nationality = self.data.get('nationality')
#         user.soo = self.data.get('soo')
#         user.lga = self.data.get('lga')
#         user.save()
#         return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'gender',
        ]
        read_only_fields = ('email',)