# from drf_spectacular.utils import extend_schema
# from rest_framework import status, permissions
# from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, ListAPIView, \
#     ListCreateAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from apps.models import Sale, HomeCategory, Home, Advertisement, HomeNeed, HomeImages, PhoneVerification, User
# from apps.serializers import SaleSerializer, HomeCategorySerializer, HomeSerializer, AdvertisementSerializer, \
#     HomeNeedSerializer, HomeImagesSerializer, PhoneVerificationSerializer, UserSerializer
#
#
# @extend_schema(tags=['sale'])
# class SaleCreateApiView(CreateAPIView):
#     queryset = Sale.objects.all()
#     serializer_class = SaleSerializer
#
#
# @extend_schema(tags=['sale'])
# class SaleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Sale.objects.all()
#     serializer_class = SaleSerializer
#
#
# @extend_schema(tags=['homecategory'])
# class HomeCategoryCreateApiView(CreateAPIView):
#     queryset = HomeCategory.objects.all()
#     serializer_class = HomeCategorySerializer
#
#
# @extend_schema(tags=['homecategory'])
# class HomeCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = HomeCategory.objects.all()
#     serializer_class = HomeCategorySerializer
#
#
# @extend_schema(tags=['home'])
# class HomeCreateApiView(ListCreateAPIView):
#     queryset = Home.objects.all()
#     serializer_class = HomeSerializer
#
#
#
#
# @extend_schema(tags=['home'])
# class HomeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Home.objects.all()
#     serializer_class = HomeSerializer
#
#
# @extend_schema(tags=['advertisement'])
# class AdvertisementCreateApiView(CreateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#
#
# @extend_schema(tags=['advertisement'])
# class AdvertisementRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#
#
# @extend_schema(tags=['homeneed'])
# class HomeNeededCreateApiView(CreateAPIView):
#     queryset = HomeNeed.objects.all()
#     serializer_class = HomeNeedSerializer
#
#
# @extend_schema(tags=['homeneed'])
# class HomeNeedRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = HomeNeed.objects.all()
#     serializer_class = HomeNeedSerializer
#
#
# @extend_schema(tags=['homeimages'])
# class HomeImageCreateApiView(CreateAPIView):
#     queryset = HomeImages.objects.all()
#     serializer_class = HomeImagesSerializer
#
#
# @extend_schema(tags=['homeimages'])
# class HomeImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = HomeImages.objects.all()
#     serializer_class = HomeImagesSerializer
#
#
# class PhoneVerificationView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = PhoneVerificationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'SMS code sent'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class VerifyCodeView(APIView):
#     def post(self, request, *args, **kwargs):
#         phone_number = request.data.get('phone_number')
#         code = request.data.get('code')
#
#         try:
#             verification = PhoneVerification.objects.get(phone_number=phone_number, code=code)
#             verification.is_verified = True
#             verification.save()
#             return Response({'message': 'Phone number verified'}, status=status.HTTP_200_OK)
#         except PhoneVerification.DoesNotExist:
#             return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# # @extend_schema(tags=['filter'])
# # class FilteredHomeAPIView(APIView):
# #
# #     def get(self, request, *args, **kwargs):
# #         home_type = request.query_params.get('type', None)
# #         location = request.query_params.get('location', None)
# #
# #         homes = Home.objects.all()
# #
# #         if home_type:
# #             homes = homes.filter(type=home_type)
# #
# #         if location:
# #             homes = homes.filter(location=location)
# #
# #         serializer = HomeSerializer(homes, many=True)
# #         return Response(serializer.data)
#
#
# @extend_schema(tags=['profile-update'])
# class UserUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.AllowAny,)
#
#
# @extend_schema(tags=['filter-home'])
# class HomeFilterListView(ListCreateAPIView):
#     serializer_class = HomeSerializer
#
#     def get_queryset(self):
#         district = self.request.query_params.get('district', None)
#         location = self.request.query_params.get('location', None)
#
#         queryset = Home.objects.all()
#
#         if district is not None:
#             queryset = queryset.filter(district__iexact=district)
#
#         if location is not None:
#             queryset = queryset.filter(location__iexact=location)
#
#         return queryset
from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions, status
from rest_framework.generics import UpdateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import HomeCategory, Home, HomeImages, HomeNeed, Advertisement, User, District, Region
from apps.serializers import HomeCategorySerializer, HomeSerializer, HomeImagesSerializer, HomeNeedSerializer, \
    AdvertisementSerializer, UserSerializer, DistrictSerializer, RegionSerializer, RegisterSerializer


@extend_schema(tags=["Home-Category"])
class HomeCategoryViewSet(viewsets.ModelViewSet):
    queryset = HomeCategory.objects.all()
    serializer_class = HomeCategorySerializer


@extend_schema(tags=["Home"])
class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def get_queryset(self):
        queryset = Home.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


@extend_schema(tags=["Home-images"])
class HomeImageViewSet(viewsets.ModelViewSet):
    queryset = HomeImages.objects.all()
    serializer_class = HomeImagesSerializer


@extend_schema(tags=["Home-needs"])
class HomeNeedViewSet(viewsets.ModelViewSet):
    queryset = HomeNeed.objects.all()
    serializer_class = HomeNeedSerializer


@extend_schema(tags=["Advertisement"])
class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


@extend_schema(tags=["UserProfileUpdate"])
class UserProfileUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)


@extend_schema(tags=['districts'])
class DistrictListView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


@extend_schema(tags=['regions'])
class RegionListView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


@extend_schema(tags=['register'])
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#   bu sayt orqali qillinadi register
# http://localhost:8000/api/v1/api/register/  json ko`rinishda beriladi
#
# {
#   "email": "user@example.com",
#   "password": "yourpassword"
# }




class HomeFilter(FilterSet):
    district = ModelChoiceFilter(queryset=District.objects.all())
    location = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Home
        fields = ['district', 'location']


@extend_schema(tags=['filter-home'])
class HomeListAPIView(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HomeFilter