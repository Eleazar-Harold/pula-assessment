from random import randint

from django.contrib.auth.models import User
from django.core.files.base import ContentFile

import factory

from sourcing.models import (
    Farm,
    Harvest,
    Resource,
)


class UserFactory(factory.django.DjangoModelFactory):
    is_active = True
    email = factory.Sequence("user-{}@example.com".format)
    username = factory.Sequence("User {}".format)
    password = factory.PostGenerationMethodCall("set_password", None)
    last_name = factory.Sequence("Last {}".format)
    first_name = factory.Sequence("First {}".format)

    class Meta:
        model = User


class FarmFactory(factory.django.DjangoModelFactory):
    is_active = True
    name = factory.Sequence("Farm {}".format)
    owner = factory.SubFactory(UserFactory)
    size = randint(101, 200)
    crop = factory.Sequence("Crop {}".format)
    town = factory.Sequence("Town {}".format)
    created_by = factory.SubFactory(UserFactory)

    class Meta:
        model = Farm


class HarvestFactory(factory.django.DjangoModelFactory):
    farm = factory.SubFactory(FarmFactory)
    harvest_weight = randint(101, 200)
    dry_weight = randint(1, 100)
    created_by = factory.SubFactory(UserFactory)

    class Meta:
        model = Harvest


class ResourceFactory(factory.django.DjangoModelFactory):
    harvest = factory.SubFactory(HarvestFactory)
    name = factory.Sequence("Image {}".format)
    image = image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {
                    "width": 1024,
                    "height": 768,
                },
            ),
            "example.jpg",
        )
    )
    created_by = factory.SubFactory(UserFactory)

    class Meta:
        model = Resource
