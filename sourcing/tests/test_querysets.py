from django.test import TestCase

from .factories import FarmFactory, HarvestFactory, ResourceFactory, UserFactory

from ..models import Farm, Harvest, Resource, User



class TestFarmQueryset(TestCase):
    manager = Farm.objects

    def test_active(self):
        """Only farms that are active"""
        user = UserFactory.create()
        farm = FarmFactory.create(owner=user)

        expected = {farm}
        self.assertSequenceEqual(set(self.manager.active()), expected)

    def test_with_harvests(self):
        """Only farm with harvests"""
        user = UserFactory.create()
        farm = FarmFactory.create(owner=user)
        FarmFactory.create(owner=user)
        harvest = HarvestFactory.create(farm=farm)
        HarvestFactory.create(farm=farm)

        expected = {farm}
        self.assertSequenceEqual(set(self.manager.with_harvests()), expected)


class TestHarvestQueryset(TestCase):
    manager = Harvest.objects

    def test_for_farm(self):
        """Only farms that are active"""
        user = UserFactory.create()
        farm = FarmFactory.create(owner=user)
        harvest = HarvestFactory.create(farm=farm)
        harvest_ii = HarvestFactory.create(farm=farm)
        harvest_iii = HarvestFactory.create(farm=farm)

        expected = {harvest, harvest_ii, harvest_iii}
        self.assertSequenceEqual(set(self.manager.for_farm(farm)), expected)

    def test_with_resources(self):
        """Only farm with harvests"""
        user = UserFactory.create()
        farm = FarmFactory.create(owner=user)
        FarmFactory.create(owner=user)
        harvest = HarvestFactory.create(farm=farm)
        harvest_ii = HarvestFactory.create(farm=farm)
        harvest_iii = HarvestFactory.create(farm=farm)
        resource = ResourceFactory.create(harvest=harvest_ii)
        resource_ii = ResourceFactory.create(harvest=harvest)

        expected = {harvest, harvest_ii}
        self.assertSequenceEqual(set(self.manager.with_resources()), expected)


class TestResourceQueryset(TestCase):
    manager = Resource.objects

    def test_for_harvest(self):
        """[summary]"""
        user = UserFactory.create()
        farm = FarmFactory.create(owner=user)
        FarmFactory.create(owner=user)
        harvest = HarvestFactory.create(farm=farm)
        harvest_ii = HarvestFactory.create(farm=farm)
        harvest_iii = HarvestFactory.create(farm=farm)
        resource = ResourceFactory.create(harvest=harvest_ii)
        resource_ii = ResourceFactory.create(harvest=harvest)

        expected = {resource_ii}
        self.assertSequenceEqual(set(self.manager.for_harvest(harvest)), expected)

