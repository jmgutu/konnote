from rest_framework import serializers
from django.conf import settings
from endusers.serializer import CustomerSerializer
from subjects.models import Subject


class SubjectSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=250)
    created_by = serializers.IntegerField()
    date_created = serializers.DateTimeField()
    modified_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.name)
        instance.save()
        return instance
