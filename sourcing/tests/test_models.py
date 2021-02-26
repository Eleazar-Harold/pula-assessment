from django.test import TestCase

from .factories import FarmFactory, HarvestFactory, ResourceFactory, UserFactory


class TestFarm(TestCase):
    def test_str(self):
        farm = FarmFactory.create()
        self.assertEqual(
            str(farm),
            f"{farm.name}-{farm.owner.username}",
        )
        self.assertIsNotNone(farm.id)
        self.assertTrue(farm.is_active)


class TestHarvest(TestCase):
    def test_str(self):
        harvest = HarvestFactory.create()
        self.assertEqual(
            str(harvest),
            f"{harvest.farm.name}",
        )
        self.assertIsNotNone(harvest.id)


class TestResource(TestCase):
    def test_str(self):
        resource = ResourceFactory.create()
        self.assertEqual(str(resource), f"{resource.name}")
        self.assertIsNotNone(resource.id)


class TestUser(TestCase):
    def test_str(self):
        user = UserFactory.create()
        self.assertEqual(str(user), f"{user.username}")
        self.assertIsNotNone(user.id)
