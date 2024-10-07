import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.models import HomeCategory, Home, HomeImages, HomeNeed, Advertisement, District, Region


@pytest.fixture
def region_fixture():
    return Region.objects.first()

@pytest.fixture
def district_fixture(region_fixture):
    return District.objects.filter(region=region_fixture).first()

@pytest.fixture
def home_category_fixture():
    HomeCategory.objects.create(type=HomeCategory.Type.YARD)
    HomeCategory.objects.create(type=HomeCategory.Type.DACHA)
    HomeCategory.objects.create(type=HomeCategory.Type.COTTAGE)

@pytest.fixture
def home_fixture(home_category_fixture, district_fixture):
    return Home.objects.create(
        location="Rakat 5",
        about="Ajoyib joy",
        type=Home.Type.HOME,
        home_category=home_category_fixture,
        district=district_fixture,
        status=Home.Status.FOR_SALE
    )

@pytest.fixture
def home_images(home_fixture):
    image_file = SimpleUploadedFile("img.png", b"file_content", content_type="image/png")
    HomeImages.objects.create(image=image_file, home=home_fixture)


@pytest.fixture
def home_need(home_fixture):
    HomeNeed.objects.create(room_count=2, length=100, price=100000, floor=3, build_with='Gisht',
                            repair=HomeNeed.RepairType.EURO,
                            home=home_fixture)


@pytest.fixture
def advertisement(home_fixture):
    video = SimpleUploadedFile("video.mp4", b"file_content", content_type="video/mp4")
    Advertisement.objects.create(video=video, home=home_fixture)
