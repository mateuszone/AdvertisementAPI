from django.test import TestCase
import json
from django.contrib.auth.models import User
from django.urls import reverse
from API.models import Category, Offer
from rest_framework.test import APITestCase
from rest_framework import status
from API.serializers import CategorySerializer, OfferMIniSerializer, OfferSerializer
from API.factories import CategoryFactory, OfferFactory


class CategoryViewSetTestCase(APITestCase):
    list_url = reverse("Category-list")

    def setUp(self):
        self.category = CategoryFactory()

    def test_category_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_category_detail_retrieve(self):
        response = self.client.get(reverse("Category-detail", kwargs={"pk": self.category.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_update(self):
        response = self.client.put(reverse("Category-detail", kwargs={"pk": self.category.id}),
                                   {"name": "Insert"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {"id": 1, "name": "Insert"})

    def test_profile_delete(self):
        response = self.client.delete(reverse("Category-detail", kwargs={"pk": self.category.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class OffersViewSetTestCase(APITestCase):
    list_url = reverse("Offers-list")

    def setUp(self):
        self.category = CategoryFactory()
        self.offer = OfferFactory()

    def test_offer_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_offer_detail_retrieve(self):
        response = self.client.get(reverse("Offers-detail", kwargs={"pk": self.offer.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_offer_update(self):
        response = self.client.put(reverse("Offers-detail", kwargs={"pk": self.offer.id}),
                                   {"title": "Insert", "description": "description",
                                    "price": 23.11, "category": self.category.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_delete(self):
        response = self.client.delete(reverse("Offers-detail", kwargs={"pk": self.offer.id}))
        self.assertEqual(response.data, 'Offer successfully deleted')
