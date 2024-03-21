from rest_framework import serializers
from rest_framework.response import Response

from contact.models import ContactLink, About, ContactModel


class ContactLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactLink
        fields='__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=About
        fields='__all__'

    def create(self, validated_data):
        return About.objects.create(**validated_data)

    def update(self, instance, validated_data):
        name=validated_data.get("name", instance.name)
        email = validated_data.get("email", instance.email)
        website = validated_data.get("website", instance.website)
        instance.save()
        return instance

class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactModel
        fields='__all__'
    def update(self, instance, validated_data):
        name=validated_data.get("name", instance.name)
        email = validated_data.get("email", instance.email)
        website = validated_data.get("website", instance.website)
        instance.save()
        return instance

