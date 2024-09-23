from rest_framework.serializers import ModelSerializer

from apps.models import Sale, HomeCategory, Home, Advertisement, HomeNeed, HomeImages


class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class HomeCategorySerializer(ModelSerializer):
    class Meta:
        model = HomeCategory
        fields = '__all__'

class HomeSerializer(ModelSerializer):
    class Meta:
        model = Home
        exclude = ('slug',)

class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'

class HomeNeedSerializer(ModelSerializer):
    class Meta:
        model = HomeNeed
        fields = '__all__'

class HomeImagesSerializer(ModelSerializer):
    class Meta:
        model = HomeImages
        fields = '__all__'