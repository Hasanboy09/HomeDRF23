from os.path import join

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.serializers import *
from root.settings import BASE_DIR


@pytest.mark.django_db
def test_sale_serializer():
    sale = Sale.objects.create(for_sale='Sotuv', for_rent='Ijara')
    serializer = SaleSerializer(sale)
    data = serializer.data
    assert data['for_sale'] == 'Sotuv'
    assert data['for_rent'] == 'Ijara'


@pytest.mark.django_db
def test_home_category_serializer():
    sale = Sale.objects.create(for_sale='Sotuv', for_rent='Ijara')
    home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
    serializer = HomeCategorySerializer(home_category)
    data = serializer.data
    assert data['type'] == HomeCategory.Type.YARD
    assert data['sale'] == sale.id



@pytest.mark.django_db
def test_home_serializer():
    sale = Sale.objects.create(
        for_sale='For Sale Example',
        for_rent='For Rent Example'
    )
    home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
    home = Home.objects.create(
        location='Location',
        about='About',
        type=Home.Type.HOME,
        home_category=home_category
    )
    serializer = HomeSerializer(home)
    data = serializer.data
    assert data['location'] == 'Location'
    assert data['about'] == 'About'
    assert data['type'] == Home.Type.HOME
    assert data['home_category'] == home_category.id


@pytest.mark.django_db
def test_home_need_serializer():
    sale = Sale.objects.create(for_sale='Some value', for_rent='Some value')

    home_category = HomeCategory.objects.create(
        type=HomeCategory.Type.YARD,
        sale=sale
    )

    home = Home.objects.create(
        location='Location',
        about='About',
        type=Home.Type.HOME,
        home_category=home_category
    )

    home_need = HomeNeed.objects.create(
        room_count=3,
        length=120.5,
        price=150000,
        floor=2,
        build_with='Brick',
        repair=HomeNeed.RepairType.MIDDLE,
        home=home
    )

    serializer = HomeNeedSerializer(home_need)
    data = serializer.data

    assert data['room_count'] == 3
    assert data['length'] == 120.5
    assert data['price'] == 150000
    assert data['floor'] == 2
    assert data['build_with'] == 'Brick'
    assert data['repair'] == HomeNeed.RepairType.MIDDLE


@pytest.mark.django_db
def test_home_images_serializer():
    sale = Sale.objects.create(for_sale='Sotuv', for_rent='Ijara')
    home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
    home = Home.objects.create(location='Location', about='About', home_category=home_category)
    with open(join(BASE_DIR, 'img.png'), 'rb') as f:
        image_file = SimpleUploadedFile(
            name='img.png',
            content=f.read(),
            content_type='image/png'
        )
        home_image = HomeImages.objects.create(image=image_file, home=home)
    serializer = HomeImagesSerializer(home_image)
    data = serializer.data
    assert data['image'] is not None
    assert data['home'] == home.id
    assert data['image'].endswith('png')


@pytest.mark.django_db
def test_advertisement_serializer():
    sale = Sale.objects.create(for_sale='Sotuv', for_rent='Ijara')
    home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD , sale=sale)
    home = Home.objects.create(location='Location', about='About', home_category=home_category)
    with open(join(BASE_DIR, 'video.mp4'), 'rb') as f:
        video_file = SimpleUploadedFile(
            name='test_video.mp4',
            content=f.read(),
            content_type='video/mp4'
        )
        advertisement = Advertisement.objects.create(video=video_file, home=home)
    serializer = AdvertisementSerializer(advertisement)
    data = serializer.data
    assert data['video'] is not None
    assert data['home'] == home.id
    assert data['video'].endswith('.mp4')
