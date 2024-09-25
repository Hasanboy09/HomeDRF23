# Create your views here.
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Sale, HomeCategory, Home, Advertisement, HomeNeed, HomeImages, PhoneVerification
from apps.serializers import SaleSerializer, HomeCategorySerializer, HomeSerializer, AdvertisementSerializer, \
    HomeNeedSerializer, HomeImagesSerializer, PhoneVerificationSerializer


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



class PhoneVerificationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PhoneVerificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'SMS code sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        try:
            verification = PhoneVerification.objects.get(phone_number=phone_number, code=code)
            verification.is_verified = True
            verification.save()
            return Response({'message': 'Phone number verified'}, status=status.HTTP_200_OK)
        except PhoneVerification.DoesNotExist:
            return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)


class FilteredHomeAPIView(APIView):

    def get(self, request, *args, **kwargs):
        home_type = request.query_params.get('type', None)
        location = request.query_params.get('location', None)

        homes = Home.objects.all()

        if home_type:
            homes = homes.filter(type=home_type)

        if location:
            homes = homes.filter(location=location)

        serializer = HomeSerializer(homes, many=True)
        return Response(serializer.data)