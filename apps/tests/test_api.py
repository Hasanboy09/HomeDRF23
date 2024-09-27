import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from apps.models import Home, HomeCategory, Sale


@pytest.mark.django_db
class TestHomeFilterListView:
    @pytest.fixture
    def setup_homes(self):
        sale = Sale.objects.create(for_sale='Sotish uchun' , for_rent='Ijara')
        category = HomeCategory.objects.create(type=HomeCategory.Type.YARD , sale=sale)

        Home.objects.create(location="Tashkent",home_category=category)
        Home.objects.create(location="Samarkand" ,home_category=category)
        Home.objects.create(location="Tashkent", home_category=category)

    def test_home_filter_by_location(self, setup_homes):
        client = APIClient()
        url = reverse('filter-home-list')
        response = client.get(url, {'location': 'Tashkent'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_home_filter_without_location(self, setup_homes):
        client = APIClient()
        url = reverse('filter-home-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3
