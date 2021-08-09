from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.response import Response

from API.models import Category, Offer
from API.serializers import CategorySerializer, OfferMIniSerializer, OfferSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']


class OffersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all CRUD operations on Offers Model.
    """
    # queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned Offers to a given Category,
        by filtering against a `category` query parameter in the URL.
        """
        queryset = Offer.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = Offer.objects.filter(category=category)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = OfferMIniSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        offer = self.get_object()
        offer.delete()
        return Response('Offer successfully deleted')
