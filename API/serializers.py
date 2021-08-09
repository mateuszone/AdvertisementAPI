from rest_framework import serializers
from API.models import Category, Offer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class OfferMIniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'title', 'price', 'category')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'title', 'description', 'price', 'created_at', 'category')
