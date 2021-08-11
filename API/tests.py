from django.test import TestCase
import json
from django.contrib.auth.models import User
from django.urls import reverse
from API.models import Category, Offer
from rest_framework.test import APITestCase
from rest_framework import status
from API.serializers import CategorySerializer, OfferMIniSerializer, OfferSerializer


class CategoryViewSetTestCase(APITestCase):
    list_url = reverse("Category-list")

    def setUp(self):
        self.name = Category.objects.create(name="Insert1")

    def test_category_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_category_detail_retrieve(self):
        response = self.client.get(reverse("Category-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_update(self):
        response = self.client.put(reverse("Category-detail", kwargs={"pk": 1}),
                                   {"name": "Insert"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {"id": 1, "name": "Insert"})

    def test_profile_delete(self):
        response = self.client.delete(reverse("Category-detail", kwargs={"pk": 1}))
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class OffersViewSetTestCase(APITestCase):
    list_url = reverse("Offers-list")

    def setUp(self):
        category = Category.objects.create(name="Insert")
        self.offer = Offer.objects.create(title="TestOffer",
                                          description="description",
                                          price=23.12,
                                          category=category)

    def test_offer_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_offer_detail_retrieve(self):
        response = self.client.get(reverse("Offers-detail", kwargs={"pk": 1}))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_offer_update(self):
        category = Category.objects.create(name="Insert1")
        response = self.client.put(reverse("Offers-detail", kwargs={"pk": 1}),
                                   {"title": "Insert", "description": "description",
                                    "price": 23.11, "category": 1})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_delete(self):
        response = self.client.delete(reverse("Offers-detail", kwargs={"pk": 1}))
        self.assertEqual(response.data, 'Offer successfully deleted')
