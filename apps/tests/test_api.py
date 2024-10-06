# import pytest
# from rest_framework import status
# from rest_framework.test import APIClient
# from django.urls import reverse
#
# from apps.models import Sale, HomeCategory, Region, District, Home
#
#
# @pytest.mark.django_db
# class TestHomeFilterListView:
#     @pytest.fixture
#     def setup_homes(self):
#         sale = Sale.objects.create(for_sale='Sotish uchun', for_rent='Ijara')
#         category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
#         region = Region.objects.create(name='Sirdaryo')
#         district1 = District.objects.create(region=region, name='Toshkent')
#         district2 = District.objects.create(region=region, name='Samarkand')
#         Home.objects.create(location="Tashkent", home_category=category, district=district1)
#         Home.objects.create(location="Samarkand", home_category=category, district=district2)
#         Home.objects.create(location="Tashkent", home_category=category, district=district1)
#
#     def test_home_filter_by_location(self, setup_homes):
#         client = APIClient()
#         url = reverse('filter-home-list')
#         response = client.get(url, {'location': 'Tashkent'})
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.data) == 2
#
#     def test_home_filter_by_district(self, setup_homes):
#         client = APIClient()
#         url = reverse('filter-home-list')
#         response = client.get(url, {'district': 'Toshkent'})
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.data) == 2
#
#     def test_home_filter_by_both(self, setup_homes):
#         client = APIClient()
#         url = reverse('filter-home-list')
#         response = client.get(url, {'location': 'Tashkent', 'district': 'Toshkent'})
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.data) == 2
#
#     def test_home_filter_without_params(self, setup_homes):
#         client = APIClient()
#         url = reverse('filter-home-list')
#         response = client.get(url)
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.data) == 3


