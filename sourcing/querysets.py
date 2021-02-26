from django.db import models


class FarmQueryset(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def with_harvests(self):
        return self.filter(harvests__isnull=False)


class HarvestQueryset(models.QuerySet):
    def for_farm(self, farm):
        return self.filter(farm=farm)

    def with_resources(self):
        return self.filter(resources__isnull=False)


class ResourceQueryset(models.QuerySet):
    def for_harvest(self, harvest):
        return self.filter(harvest=harvest)
