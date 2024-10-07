import pytest

from apps.models import HomeCategory, Home, HomeImages, HomeNeed, Advertisement


@pytest.fixture
def home_category():
    HomeCategory.objects.create(type='Dacha')
    HomeCategory.objects.create(type='Cottage')


@pytest.fixture
def home(home_category):
    Home.objects.create(location='Rakat 5', about='Ajoyib', type='Home', home_category=home_category, slug='home',
                        district=169, status='For Rent')


@pytest.fixture
def home_images(home):
    HomeImages.objects.create(image='img.png', home=home)


@pytest.fixture
def home_need(home):
    HomeNeed.objects.create(room_count=2, length=100, price=100000, floor=3, build_with='Gisht', repair='Euro',
                            home=home)


@pytest.fixture
def advertisement(home):
    Advertisement.objects.create(video='video.mp4', home=home)
