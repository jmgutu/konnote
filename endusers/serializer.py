from rest_framework import serializers
from django.conf import settings
from endusers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('website_url','email', 'physical_address', 'postal_code', 'mobile', 'telephone', 'postal_address',
                  'country', 'county', 'bio', 'birth_date', 'gender', 'email_verification_code',
                  'email_verification_generation_date', 'email_verification_date', 'mobile_verified',
                  'mobile_verification_code', 'mobile_verification_generation_date', 'mobile_verification_date',
                  'email_verified', 'created_by', 'date_created', 'modified_date', 'profilephoto',)


