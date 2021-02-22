from collections import defaultdict

from django.db import models


class FarmQueryset(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def with_harvests(self):
        return self.filter(harvests__isnull=False)


class HarvestQueryset(models.QuerySet):
    def compare(self):
        if self.harvest_weight < self.dry_weight:
            return error("harvest weight cannot be less that dry weight")
        return self

    def for_farm(self, farm):
        return self.filter(farm=farm)

    def with_resources(self):
        return self.filter(resources__isnull=False)
