from django.contrib.auth.models import User

from rest_framework import serializers

# from rest_framework.authtoken.models import Token

from sourcing.models import (
    Farm,
    Harvest,
    Resource,
)


class ResourceSerializer(serializers.ModelSerializer):
    harvest = serializers.HyperlinkedRelatedField(view_name='harvest-detail', read_only=True)
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

    def get_validation_exclusions(self, *args, **kwargs):
        # exclude the farm field as we supply it later on in the
        # corresponding view based on the http request
        exclusions = super(ResourceSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['harvest']

    def create(self, validated_data):
        resource = Resource.objects.create(**validated_data)
        return resource


class HarvestSerializer(serializers.ModelSerializer):
    farm = serializers.HyperlinkedRelatedField(view_name='farm-detail', read_only=True)
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
    
    def get_validation_exclusions(self, *args, **kwargs):
        # exclude the farm field as we supply it later on in the
        # corresponding view based on the http request
        exclusions = super(HarvestSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['farm']

    def create(self, validated_data):
        hw = validated_data.pop("harvest_weight")
        dw = validated_data.pop("dry_weight")
        if dw > hw:
            raise serializers.ValidationError(
                {"dry_weight": "dry weight must be less than harvest weight"},
            )

        harvest = Harvest.objects.create(**validated_data)
        return harvest


class FarmSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='owner-detail', read_only=True)
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

    def get_validation_exclusions(self, *args, **kwargs):
        # exclude the farm field as we supply it later on in the
        # corresponding view based on the http request
        exclusions = super(FarmSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['owner']

    def create(self, validated_data):
        farm = Farm.objects.create(**validated_data)
        return farm


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "last_name",
            "first_name",
            "password",
            "password2",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
            "email": {"required": True},
            "username": {"required": True},
            "last_name": {"required": True},
            "first_name": {"required": True},
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationSerializer, self).__init__(*args, **kwargs)
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
        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")

        if password != password2:
            raise serializers.ValidationError({"password": "Password must match"})
        user, created = User.objects.get_or_create(**validated_data)
        if created:
            user.set_password(password)
            user.save()
        return user
