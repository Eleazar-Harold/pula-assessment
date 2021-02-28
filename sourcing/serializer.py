from django.contrib.auth.models import User

from rest_framework import serializers

# from rest_framework.authtoken.models import Token

from sourcing.models import (
    Farm,
    Harvest,
    Resource,
)


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = (
            "id",
            "name",
            "image",
            "harvest",
        )
        extra_kwargs = {
            "name": {"required": True},
            "image": {"required": True},
            "harvest": {"required": True},
        }

    def __init__(self, *args, **kwargs):
        super(ResourceSerializer, self).__init__(*args, **kwargs)
        self.fields["name"].error_messages["required"] = u"name is required"
        self.fields["name"].error_messages["blank"] = u"name cannot be blank"
        self.fields["image"].error_messages["required"] = u"image is required"
        self.fields["image"].error_messages["blank"] = u"image cannot be blank"
        self.fields["harvest"].error_messages["required"] = u"harvest is required"
        self.fields["harvest"].error_messages["blank"] = u"harvest cannot be blank"

    def create(self, validated_data):
        resource = Resource.objects.create(**validated_data)
        return resource


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = (
            "id",
            "harvest_weight",
            "dry_weight",
            "farm",
        )
        extra_kwargs = {
            "harvest_weight": {"required": True},
            "dry_weight": {"required": True},
            "farm": {"required": True},
        }

    def __init__(self, *args, **kwargs):
        super(HarvestSerializer, self).__init__(*args, **kwargs)
        self.fields["harvest_weight"].error_messages[
            "required"
        ] = u"harvest weight is required"
        self.fields["harvest_weight"].error_messages[
            "blank"
        ] = u"harvest weight cannot be blank"
        self.fields["dry_weight"].error_messages["required"] = u"dry weight is required"
        self.fields["dry_weight"].error_messages["blank"] = u"dry weight cannot be blank"
        self.fields["farm"].error_messages["required"] = u"farm is required"
        self.fields["farm"].error_messages["blank"] = u"farm cannot be blank"

    def create(self, validated_data):
        hw = validated_data.pop("harvest_weight")
        dw = validated_data.pop("dry_weight")
        if dw > hw:
            raise serializers.ValidationError(
                "dry weight must be less than harvest weight"
            )

        harvest = Harvest.objects.create(**validated_data)
        return harvest


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = (
            "id",
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

    def __init__(self, *args, **kwargs):
        super(FarmSerializer, self).__init__(*args, **kwargs)
        self.fields["name"].error_messages["required"] = u"name is required"
        self.fields["name"].error_messages["blank"] = u"name cannot be blank"
        self.fields["size"].error_messages["required"] = u"size is required"
        self.fields["size"].error_messages["blank"] = u"size cannot be blank"
        self.fields["crop"].error_messages["required"] = u"crop is required"
        self.fields["crop"].error_messages["blank"] = u"crop cannot be blank"
        self.fields["town"].error_messages["required"] = u"town is required"
        self.fields["town"].error_messages["blank"] = u"town cannot be blank"
        self.fields["owner"].error_messages["required"] = u"owner is required"
        self.fields["owner"].error_messages["blank"] = u"owner cannot be blank"

    def create(self, validated_data):
        farm = Farm.objects.create(**validated_data)
        return farm


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
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

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        self.fields["username"].error_messages["required"] = u"username is required"
        self.fields["username"].error_messages["blank"] = u"username cannot be blank"
        self.fields["email"].error_messages["required"] = u"email is required"
        self.fields["email"].error_messages["blank"] = u"email cannot be blank"
        self.fields["last_name"].error_messages["required"] = u"last name is required"
        self.fields["last_name"].error_messages["blank"] = u"last name cannot be blank"
        self.fields["first_name"].error_messages["required"] = u"first name is required"
        self.fields["first_name"].error_messages["blank"] = u"first name cannot be blank"
        self.fields["password"].error_messages[
            "min_length"
        ] = u"password must be at least 8 chars"

    def create(self, validated_data):
        """Create and return a new user."""
        passphrase = validated_data.pop("password")
        user, created = User.objects.get_or_create(**validated_data)
        if created:
            user.set_password(passphrase)
            user.save()
        return user
