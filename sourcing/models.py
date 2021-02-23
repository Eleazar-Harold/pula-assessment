from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from location_field.models.plain import PlainLocationField

from sourcing.querysets import (
    FarmQueryset,
    HarvestQueryset,
    ResourceQueryset,
)
import uuid

# Create your models here.


class Base(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=False,
        related_name="%(class)s_creates",
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_updates",
    )
    deleted = models.BooleanField(
        default=False,
    )
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_deletes",
    )

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(Base, self).delete()


class Farm(Base):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User,
        related_name=_("farms"),
        on_delete=models.CASCADE,
    )
    size = models.IntegerField()
    crop = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    location = PlainLocationField(
        based_fields=["town"],
        zoom=7,
    )
    is_active = models.BooleanField(default=True)

    objects = FarmQueryset.as_manager()


class Harvest(Base):
    farm = models.ForeignKey(
        Farm,
        related_name=_("harvests"),
        on_delete=models.CASCADE,
    )
    harvest_weight = models.DecimalField(
        max_digits=19,
        decimal_places=7,
        default=1,
    )
    dry_weight = models.DecimalField(
        max_digits=19,
        decimal_places=7,
        default=1,
    )

    objects = HarvestQueryset.as_manager()


class Resource(Base):
    name = models.CharField(max_length=50)
    harvest = models.ForeignKey(
        Harvest,
        related_name=_("resources"),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="resources")

    objects = ResourceQueryset.as_manager()
