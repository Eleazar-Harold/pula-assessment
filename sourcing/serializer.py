from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from sourcing.models import (
    Farm,
    Harvest,
    Resource,
)


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = (
            "name",
            "image",
            "harvest",
        )
        extra_kwargs = {
            "name": {"required": True},
            "image": {"required": True},
            "harvest": {"required": True},
        }

    def create(self, validated_data):
        resource = Resource.objects.create(**validated_data)
        return resource


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = (
            "harvest_weight",
            "dry_weight",
            "farm",
        )
        extra_kwargs = {
            "harvest_weight": {"required": True},
            "dry_weight": {"required": True},
            "farm": {"required": True},
        }

    def create(self, validated_data):
        harvest = Harvest.objects.create(**validated_data)
        return harvest


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = (
            "name",
            "size",
            "crop",
            "town",
            "owner",
        )
        extra_kwargs = {
            "name": {"required": True},
            "size": {"required": True},
            "crop": {"required": True},
            "town": {"required": True},
            "owner": {"required": True},
        }

    def create(self, validated_data):
        farm = Farm.objects.create(**validated_data)
        return farm


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "last_name",
            "first_name",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "username": {"required": True},
            "last_name": {"required": True},
            "first_name": {"required": True},
        }

    def create(self, validated_data):
        """Create and return a new user."""
        passphrase = validated_data.pop("password")
        user, created = User.objects.get_or_create(**validated_data)
        if created:
            user.set_password(passphrase)
            user.save()
        return user
