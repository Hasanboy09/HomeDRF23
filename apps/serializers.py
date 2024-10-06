from rest_framework import serializers

from apps.models import HomeCategory, HomeImages, Home, HomeNeed, Advertisement, District, User, Region


class HomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCategory
        fields = ['id', 'type']


class HomeImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeImages
        fields = ['id', 'image', 'home']


class HomeNeedSerializer(serializers.ModelSerializer):
    home = serializers.PrimaryKeyRelatedField(queryset=Home.objects.all())

    class Meta:
        model = HomeNeed
        fields = ['id', 'room_count', 'length', 'price', 'floor', 'build_with', 'repair', 'home']


class HomeSerializer(serializers.ModelSerializer):
    home_category = serializers.PrimaryKeyRelatedField(queryset=HomeCategory.objects.all())
    district = serializers.PrimaryKeyRelatedField(queryset=District.objects.all())
    needs = HomeNeedSerializer(many=True, read_only=True)

    images = HomeImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Home
        fields = ['id', 'location', 'about', 'type', 'home_category', 'district', 'status', 'needs', 'images']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

    def validate_district(self, value):
        if not value:
            raise serializers.ValidationError("District is required.")
        return value


class AdvertisementSerializer(serializers.ModelSerializer):
    home = HomeSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ['id', 'video', 'home']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'image', 'first_name', 'last_name', 'email'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
