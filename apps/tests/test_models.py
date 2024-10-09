from apps.tests.test_fixture import *


@pytest.mark.django_db
def test_home_category_model(home_category_fixture):
    home_category_fixture = HomeCategory.objects.get(type=HomeCategory.Type.DACHA)
    assert home_category_fixture.type == HomeCategory.Type.DACHA
    assert home_category_fixture.id == 2


@pytest.mark.django_db
def test_home_creation(district_fixture):
    district_fixture = District.objects.first()
    home_category = HomeCategory.objects.create(type=HomeCategory.Type.COTTAGE)
    home = Home.objects.create(
        location="Oq saroy",
        about="Shinam saroy",
        type=Home.Type.RENT,
        home_category=home_category,
        district=district_fixture,
        status=Home.Status.FOR_RENT
    )

    assert home.location == "Oq saroy"
    assert home.type == Home.Type.RENT
    assert home.status == Home.Status.FOR_RENT
    assert home.district == district_fixture
