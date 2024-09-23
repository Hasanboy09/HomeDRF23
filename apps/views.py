from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from apps.models import Sale, HomeCategory, Home, Advertisement, HomeNeed, HomeImages
from apps.serializers import SaleSerializer, HomeCategorySerializer, HomeSerializer, AdvertisementSerializer, \
    HomeNeedSerializer, HomeImagesSerializer


@extend_schema(tags=['sale'])
class SaleCreateApiView(CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


@extend_schema(tags=['sale'])
class SaleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


@extend_schema(tags=['homecategory'])
class HomeCategoryCreateApiView(CreateAPIView):
    queryset = HomeCategory.objects.all()
    serializer_class = HomeCategorySerializer


@extend_schema(tags=['homecategory'])
class HomeCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = HomeCategory.objects.all()
    serializer_class = HomeCategorySerializer


@extend_schema(tags=['home'])
class HomeCreateApiView(CreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


@extend_schema(tags=['home'])
class HomeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


@extend_schema(tags=['advertisement'])
class AdvertisementCreateApiView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


@extend_schema(tags=['advertisement'])
class AdvertisementRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


@extend_schema(tags=['homeneed'])
class HomeNeededCreateApiView(CreateAPIView):
    queryset = HomeNeed.objects.all()
    serializer_class = HomeNeedSerializer


@extend_schema(tags=['homeneed'])
class HomeNeedRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = HomeNeed.objects.all()
    serializer_class = HomeNeedSerializer


@extend_schema(tags=['homeimages'])
class HomeImageCreateApiView(CreateAPIView):
    queryset = HomeImages.objects.all()
    serializer_class = HomeImagesSerializer

@extend_schema(tags=['homeimages'])
class HomeImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = HomeImages.objects.all()
    serializer_class = HomeImagesSerializer
