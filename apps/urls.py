from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import HomeCategoryViewSet, HomeViewSet, HomeImageViewSet, HomeNeedViewSet, AdvertisementViewSet, \
    UserProfileUpdateView, DistrictListView, RegionListView, RegisterView, HomeListAPIView

router = DefaultRouter()
router.register('home-categories', HomeCategoryViewSet, basename='home-categories')
router.register('homes', HomeViewSet, basename='homes')
router.register('home-images', HomeImageViewSet, basename='home-images')
router.register('home-needs', HomeNeedViewSet, basename='home-needs')
router.register('advertisements', AdvertisementViewSet, basename='advertisements')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('users/<int:pk>/profile/', UserProfileUpdateView.as_view(), name='user-profile-update'),

    path('district', DistrictListView.as_view(), name='district-list'),
    path('regions', RegionListView.as_view(), name='region-list'),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', RegisterView.as_view(), name='register'),

    path('filter-homes/', HomeListAPIView.as_view(), name='filter-home-list'),
]
