from rest_framework.serializers import ModelSerializer

from apps.models import Sale, HomeCategory, Home, Advertisement, HomeNeed, HomeImages, PhoneVerification
from apps.utils import send_sms


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
        fields = '__all__'


class HomeNeedSerializer(ModelSerializer):
    class Meta:
        model = HomeNeed
        fields = ['room_count', 'length', 'price', 'floor', 'build_with', 'repair']


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class HomeImagesSerializer(ModelSerializer):
    class Meta:
        model = HomeImages
        fields = ['image', 'home']


class PhoneVerificationSerializer(ModelSerializer):
    class Meta:
        model = PhoneVerification
        fields = '__all__'

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        verification, created = PhoneVerification.objects.get_or_create(phone_number=phone_number)
        verification.generate_code()
        send_sms(phone_number, verification.code)
        return verification
