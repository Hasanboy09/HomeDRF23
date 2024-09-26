from django.urls import path

from apps.views import *

urlpatterns = [
    path('sale', SaleCreateApiView.as_view(), name='sale-create'),
    path('sale/<int:pk>', SaleRetrieveUpdateDestroyAPIView.as_view(), name='sale-retrieve-update'),

    path('homecategory', HomeCategoryCreateApiView.as_view(), name='home-category-create'),
    path('homecategory/<int:pk>', HomeCategoryRetrieveUpdateDestroyAPIView.as_view(),
         name='home-category-retrieve-update'),

    path('home', HomeCreateApiView.as_view(), name='home-create'),
    path('home/<int:pk>', HomeRetrieveUpdateDestroyAPIView.as_view(), name='home-retrieve-update'),
    path('home' , HomeCreateApiView.as_view(), name='home-list'),

    path('advertisement', AdvertisementCreateApiView.as_view(), name='advertisement-create'),
    path('advertisement/<int:pk>', AdvertisementRetrieveUpdateDestroyAPIView.as_view(),
         name='advertisement-retrieve-update'),

    path('homeneed', HomeNeededCreateApiView.as_view(), name='home-needed-create'),
    path('homeneed/<int:pk>', HomeNeedRetrieveUpdateDestroyAPIView.as_view(), name='home-needed-retrieve-update'),

    path('homeimage', HomeImageCreateApiView.as_view(), name='home-image-create'),
    path('homeimage/<int:pk>', HomeImageRetrieveUpdateDestroyAPIView.as_view(), name='home-image-retrieve-update'),
]

urlpatterns += [
    path('verify-phone/', PhoneVerificationView.as_view(), name='verify_phone'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify_code'),
    path('homes/', HomeFilterListView.as_view(), name='filter-home-list'),
]

urlpatterns += [
    path('user-profile/<int:pk>', UserUpdateAPIView.as_view(), name='user-profile-update'),
]
