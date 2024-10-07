import pytest

from apps.models import HomeCategory


@pytest.mark.django_db
def test_home_category_types(home_category):
    assert home_category[0].type == HomeCategory.Type.DACHA
