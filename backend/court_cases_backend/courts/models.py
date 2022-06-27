from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, name: str, surename: str, password=None, **extra_fields):
        if not email:
            raise ValueError('Пользователь должен иметь email')

        if not name:
            raise ValueError('Пользователь должен иметь имя')

        if not surename:
            raise ValueError('Пользователь должен иметь фамилия')

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            surename = surename,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, email: str, name: str, surename: str, password: None, **extra_fields):
        if not email:
            raise ValueError('Пользователь должен иметь email')

        if not name:
            raise ValueError('Пользователь должен иметь имя')

        if not surename:
            raise ValueError('Пользователь должен иметь фамилия')

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            surename = surename,
            **extra_fields,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self.db)

        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    surename = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    is_chief = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'surename']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin