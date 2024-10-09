from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField, IntegerField, Model, TextChoices, TextField, ForeignKey, CASCADE, \
    FloatField, FileField, ImageField, SlugField, DateTimeField, ManyToManyField
from django.utils.text import slugify


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
    balance = IntegerField(null=True, default=0, blank=True)
    district = ForeignKey('apps.District', on_delete=CASCADE, related_name='users', null=True, blank=True)
    image = ImageField(upload_to='users')

    def __str__(self):
        return self.first_name


class BaseModelSlug(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True  # o`zi table bo1lib yaratilmasligi kerak # noqa

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):  # noqa
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Region(Model):
    name = CharField(max_length=50)


class District(Model):
    name = CharField(max_length=50)
    region = ForeignKey('apps.Region', CASCADE, related_name='districts')



class HomeCategory(Model):
    class Type(TextChoices):
        YARD = 'Yard', 'yard'
        DACHA = 'Dacha', 'dacha'
        COTTAGE = 'Cottage', 'cottage'

    type = CharField(max_length=255, choices=Type.choices, default=Type.YARD)


class Home(Model):
    class Type(TextChoices):
        ALL_PROPERTY = 'All_property', 'all_property'
        RENT = 'Rent', 'rent'
        HOME = 'Home', 'home'
        BUSINESS = 'Business', 'business'

    class Status(TextChoices):
        FOR_SALE = 'For Sale', 'for_sale'
        FOR_RENT = 'For Rent', 'for_rent'

    location = CharField(max_length=255)
    about = TextField()
    type = CharField(max_length=255, choices=Type.choices, default=Type.ALL_PROPERTY)
    home_category = ForeignKey("apps.HomeCategory", on_delete=CASCADE, related_name='homes')
    district = ForeignKey("apps.District", on_delete=CASCADE, related_name='homes')
    status = CharField(max_length=50, choices=Status.choices, default=Status.FOR_SALE)


class HomeImages(Model):
    image = ImageField()
    home = ForeignKey('apps.Home', on_delete=CASCADE, related_name='images')


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


class Advertisement(Model):
    video = FileField(upload_to='advertisements/')
    home = ForeignKey('apps.Home', on_delete=CASCADE, related_name='advertisements')
