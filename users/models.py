import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone

from datetime import datetime



DISCOUNT_CODE_TYPES_CHOICES = [
    ('percent', 'Percentage-based'),
    ('value', 'Value-based'),
]


class MyUserManager(BaseUserManager):
    def create_user(self, username, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        # """
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
            date_of_birth=date_of_birth,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

from versatileimagefield.fields import VersatileImageField

class MyUser(AbstractBaseUser):

    # class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True, blank=True, null=True)
    image = VersatileImageField("Image", upload_to="images/", blank=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True)
    is_student = models.BooleanField(blank=True, null=True)
    is_parent = models.BooleanField(blank=True, null=True)
    is_faculty = models.BooleanField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    linkedin_token = models.TextField(blank=True, default='')
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



# class Brand(models.Model):
#     brand = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     brand_image = models.ImageField(upload_to='brand',  default='default.jpg')

#     def __str__(self):
#         return self.brand


# class Item(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.FloatField()
#     discount_price = models.FloatField(blank=True, null=True)
#     brand = models.ManyToManyField(Brand, max_length=100)
#     image = models.ImageField(upload_to='images')
#     in_stock = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title


# class CartItem(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(default=datetime.now)
#     product = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     total = models.IntegerField(default=0)
#     ordered = models.BooleanField(default=False)

#     choices = (
#         ('Received', 'Received'),
#         ('Scheduled', 'Scheduled'),
#         ('Shipped', 'Shipped'),
#         ('Failed', 'Failed'),
#         ('In Progress', 'In Progress'),
#     )

#     status = models.CharField(
#         max_length=100, choices=choices, default="In Progress")


# class Order(models.Model):

#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     items = models.ManyToManyField(CartItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     total = models.IntegerField(default=0)

#     def __str__(self):
#         return self.user.username


# class Wishlist(models.Model):

#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     wished_item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     slug = models.CharField(max_length=30, null=True, blank=True)
#     added_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.wished_item.title