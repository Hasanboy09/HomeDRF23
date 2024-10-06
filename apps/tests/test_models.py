# from os.path import join
#
# import pytest
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import Client
# from django.urls import reverse
#
# from apps.models import Sale, HomeCategory, Home, Advertisement, HomeNeed, Region, District
# from root.settings import BASE_DIR
#
#
# @pytest.mark.django_db
# def test_sale_model():
#     sale = Sale.objects.create(for_sale="Sotuv", for_rent="Ijara")
#     assert sale.for_sale == "Sotuv"
#     assert sale.for_rent == "Ijara"
#
#
# @pytest.mark.django_db
# def test_home_category_model():
#     sale = Sale.objects.create(for_sale="Sotuv", for_rent="Ijara")
#     home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
#
#     assert home_category.type == HomeCategory.Type.YARD
#     assert home_category.sale == sale
#
#
# @pytest.mark.django_db
# def test_home_model():
#     region = Region.objects.create(name='Qashqadaryo')
#     district = District.objects.create(name='Qarshi', region=region)
#     sale = Sale.objects.create(for_sale="Sotuv", for_rent="Ijara")
#     home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
#     home = Home.objects.create(location="Qarshi shahar", about="Qisqacha malumot", home_category=home_category,
#                                district=district)
#
#     assert home.location == "Qarshi shahar"
#     assert home.about == "Qisqacha malumot"
#     assert home.home_category == home_category
#
#
# @pytest.mark.django_db
# def test_advertisement_model():
#     region = Region.objects.create(name='Toshkent')
#     district = District.objects.create(name='Toshkent', region=region)
#     sale = Sale.objects.create(for_sale="Sotuv", for_rent="Ijara")
#     home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
#     home = Home.objects.create(location="Toshkent", about="Tavsif", home_category=home_category, district=district)
#
#     with open(join(BASE_DIR, 'video.mp4'), 'rb') as f:
#         video_file = SimpleUploadedFile(
#             name='video.mp4',
#             content=f.read(),
#             content_type='video/mp4'
#         )
#         advertisement = Advertisement.objects.create(video=video_file, home=home)
#
#     assert advertisement.video.name.endswith(".mp4")
#     assert "video" in advertisement.video.name
#     assert advertisement.home == home
#
#
# @pytest.mark.django_db
# def test_home_need_model():
#     region = Region.objects.create(name='Qashqadaryo')
#     district = District.objects.create(name='Kasbi Tumani', region=region)
#     sale = Sale.objects.create(for_sale="Sotuv", for_rent="Ijara")
#     home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
#     home = Home.objects.create(location="Kasbi", about="Tavsif", home_category=home_category, district=district)
#
#     home_need = HomeNeed.objects.create(
#         room_count=3,
#         length=120.5,
#         price=50000.0,
#         floor=2,
#         build_with="G'isht",
#         repair=HomeNeed.RepairType.MIDDLE,
#         home=home
#     )
#
#     assert home_need.room_count == 3
#     assert home_need.length == 120.5
#     assert home_need.price == 50000.0
#     assert home_need.floor == 2
#     assert home_need.build_with == "G'isht"
#     assert home_need.repair == HomeNeed.RepairType.MIDDLE
#
#
# @pytest.mark.django_db
# def test_home_image_create(client):
#     region = Region.objects.create(name='Toshkent')
#     district = District.objects.create(name='Yakkasaroy Tumani', region=region)
#     sale = Sale.objects.create(for_sale="Sotuv", for_rent="Ijara")
#     home_category = HomeCategory.objects.create(type=HomeCategory.Type.YARD, sale=sale)
#     home = Home.objects.create(location='Yakkasaroy', about='Biznes uchun ajoyib', home_category=home_category, district=district)
#
#     path = reverse('home-image-create')
#     with open(join(BASE_DIR, 'img.png'), 'rb') as f:
#         file = SimpleUploadedFile(
#             name='img.png',
#             content=f.read(),
#             content_type='image/png'
#         )
#         data = {
#             "image": file,
#             "home": home.id
#         }
#         response = client.post(path, data=data, format='multipart')
#
#     assert response.status_code == 201
#     assert 'image' in response.data
#     assert response.data['image'].endswith('.png')