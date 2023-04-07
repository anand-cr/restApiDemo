from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
# Create your models here.


class ApiView(models.Model):
    function = models.CharField(max_length=50)
    details = models.CharField(max_length=100)

    def __str__(self):
        return self.function

# NOTE:


class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("user must have an email address")

        # makes second half case insensitive
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # we need to use set password cuz it should be encrypted
        # set password method encrpts
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Databse model for users in the sytem"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # determine if it should have access to Django admin etc
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # Overriding the orginal username field as email, always required by default
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status feed item"""
    # allow users to store status update associated with the person who created it
    # connect to other models using foreign key
    # get the model using settings instead of hardcoding the model name
    # on_delete= cascade -> cascade the change down to remove the associated feed items ie, if we deleet the user_profile then it will delete the feeds items too
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return the model as a string"""
        return self.status_text
