
from apps.tests.test_fixture import *


@pytest.mark.django_db
def test_home_category_model(home_category_fixture):
    home_category_fixture = HomeCategory.objects.get(type=HomeCategory.Type.DACHA)
    assert home_category_fixture.type == HomeCategory.Type.DACHA
    assert home_category_fixture.id == 2

