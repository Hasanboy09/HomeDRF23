import random

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField, IntegerField, Model, TextChoices, TextField, ForeignKey, CASCADE, \
    FloatField, FileField, ImageField, SlugField, DateTimeField
from django.utils.text import slugify
from rest_framework.fields import BooleanField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Phone Number field must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    email = EmailField(unique=True)
    organization = CharField(max_length=255, blank=True, null=True)
    phone_number = CharField(max_length=255)
    balance = IntegerField()

    def __str__(self):
        return self.first_name


class BaseModelSlug(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True  # o`zi table bo1lib yaratilmasligi kerak # noqa

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None): # noqa
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Sale(Model):
    for_sale = CharField(max_length=255)
    for_rent = CharField(max_length=255)

class HomeCategory(Model):
    class Type(TextChoices):
        YARD = 'Yard', 'yard'
        DACHA = 'Dacha', 'dacha'
        COTTAGE = 'Cottage', 'cottage'

    type = CharField(max_length=255, choices=Type.choices, default=Type.YARD)
    sale= ForeignKey('apps.Sale', on_delete=CASCADE, related_name='sales')



class Home(Model):
    class Type(TextChoices):
        ALL_PROPERTY = 'All_property', 'all_property'
        RENT = 'Rent', 'rent'
        HOME = 'Home', 'home'
        BUSINESS = 'Business', 'business'

    location = CharField(max_length=255)
    about = TextField()
    type = CharField(max_length=255, choices=Type.choices, default=Type.ALL_PROPERTY)
    home_category = ForeignKey("apps.HomeCategory", on_delete=CASCADE, related_name='homes')



class Advertisement(Model):
    video = FileField(upload_to='advertisements/')
    home = ForeignKey('apps.Home', on_delete=CASCADE, related_name='advertisements')




class HomeNeed(Model):
    class RepairType(TextChoices):
        MIDDLE = 'Middle', 'middle'
        EURO = 'Euro', 'euro'
        WITHOUT_REPAIR = 'Without_Repair', 'without_repair'

    room_count = IntegerField()
    length = FloatField()
    price = FloatField()
    floor = IntegerField()
    build_with = CharField(max_length=255)
    repair = CharField(max_length=255, choices=RepairType.choices, default=RepairType.MIDDLE)
    home = ForeignKey('apps.Home', on_delete=CASCADE, related_name='needs')



class HomeImages(Model):
    image = ImageField()
    home = ForeignKey('apps.Home', on_delete=CASCADE, related_name='images')



class PhoneVerification(Model):
    phone_number = CharField(max_length=15)
    code = CharField(max_length=6)
    is_verified = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    def generate_code(self):
        self.code = str(random.randint(100000, 999999))
        self.save()