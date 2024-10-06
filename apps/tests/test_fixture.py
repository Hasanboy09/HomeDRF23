import pytest

from apps.models import Home, Sale, HomeCategory


@pytest.fixture
def sale():
    Sale.objects.create(for_sale='Uy Sotish' , for_rent='Kvartira')

@pytest.fixture
def home_category(sale):
    HomeCategory.objects.create(type='Yard' , sale_id=sale)
#
