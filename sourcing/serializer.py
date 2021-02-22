from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


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
        user, created = User.objects.get_or_create(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        if created:
            user.set_password(validated_data["password"])
            user.save()
        return user
