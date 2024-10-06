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
