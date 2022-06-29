from re import M
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# user class
class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, name: str, surename: str, password=None, **extra_fields):
        if not email:
            raise ValueError('Пользователь должен иметь email')

        if not name:
            raise ValueError('Пользователь должен иметь имя')

        if not surename:
            raise ValueError('Пользователь должен иметь фамилию')

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
    email = models.EmailField(unique=True)
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
        if self.patronymic:
            _patronymic = '{self.patronymic[0]}.'
        else:
            _patronymic = ''
        return f'{self.name} {self.surename[0]}.{_patronymic}'

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

# Courts classes

class CourtCases(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number_of_court = models.IntegerField()
    case_source_and_summ = models.CharField(max_length=255)
    case_purpose = models.CharField(max_length=255)
    claim = models.CharField(max_length=255)
    number_case_in_first_instance = models.CharField(max_length=255, blank=True)
    number_case_in_numenklature = models.CharField(max_length=255, blank=True)
    date_of_appeal = models.CharField(max_length=255, blank=True) 
    date_of_submission_appeal = models.CharField(max_length=255, blank=True)
    total_amount_recovered = models.CharField(max_length=255, blank=True)
    information_about_need_recourse = models.CharField(max_length=255, blank=True)
    summary_of_court =  models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.number_of_court} | {self.case_source_and_summ}' 


class CourtFirstInstance(models.Model):
    case_id = models.ForeignKey(CourtCases, on_delete=models.CASCADE)
    dates_of_court_hearing = models.JSONField(blank=True)
    date_of_dicision = models.DateField(blank=True, null=True)
    brief_operative_part = models.TextField(blank=True)
    minfin_information = models.CharField(max_length=255, blank=True)
    date_of_filing_in_court = models.DateField(blank=True, null=True)
    date_of_receipt_of_judgment = models.DateField(blank=True, null=True)
    date_appeal_by_the_parties = models.DateField(blank=True, null=True)
    date_appeal_to_the_court = models.DateField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)


class CourtSecondInstance(models.Model):
    case_id = models.ForeignKey(CourtCases, on_delete=models.CASCADE)
    dates_of_court_hearing = models.JSONField(blank=True)
    date_of_dicision = models.DateField(blank=True, null=True)
    brief_operative_part = models.TextField(blank=True)
    minfin_information = models.CharField(max_length=255, blank=True)
    date_of_filing_in_court = models.DateField(blank=True, null=True)
    date_of_receipt_of_judgment = models.DateField(blank=True, null=True)
    date_appeal_by_the_parties = models.DateField(blank=True, null=True)
    date_appeal_to_the_court = models.DateField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)


class CourtThirdInstance(models.Model):
    case_id = models.ForeignKey(CourtCases, on_delete=models.CASCADE)
    date_of_judgment = models.DateField(blank=True, null=True)
    brief_operative_part = models.TextField(blank=True)
    minfin_information = models.CharField(max_length=255, blank=True)
    date_of_application_court_acts = models.DateField(blank=True, null=True)
    date_of_receipt_acts = models.DateField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)


class NotifyTask(models.Model):
    court_id = models.ForeignKey(CourtCases, on_delete=models.CASCADE)
    notify_message = models.TextField()
    date_of_notify = models.DateField()
    notify_cout = models.IntegerField()
    max_count_before_chief_notify = models.IntegerField()
    chief_message = models.TextField(blank=True)
    count_update_day = models.IntegerField()