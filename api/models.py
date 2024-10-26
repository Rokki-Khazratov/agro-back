from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




#!UTILS:
class HealthStatus(models.TextChoices):
    YAHSHI = 'yahshi', 'Yahshi'
    ORTACHA = 'ortacha', 'Ortacha'
    YOMON = 'yomon', 'Yomon'




class District(models.Model):
    REGION_CHOICES = [
        ('tashkent_city', 'Ташкент (город)'),
        ('tashkent', 'Ташкентская область'),
        ('andijan', 'Андижанская область'),
        ('bukhara', 'Бухарская область'),
        ('djizzakh', 'Джиззакская область'),
        ('fergana', 'Ферганская область'),
        ('kashkadarya', 'Кашкадарьинская область'),
        ('khorezm', 'Хорезмская область'),
        ('namangan', 'Наманганская область'),
        ('navoiy', 'Навоийская область'),
        ('samarkand', 'Самаркандская область'),
        ('sirdarya', 'Сырдарьинская область'),
        ('surkhandarya', 'Сурхандарьинская область'),
        ('karakalpakstan', 'Республика Каракалпакстан'),
    ]

    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50, choices=REGION_CHOICES)

    # controller_name = models.CharField(max_length=255)
    # controller_phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}, {self.region}'


#?-----------------------------MODELS----------------------------------------
class NewsCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель для новостей
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Модель для хранения изображений, связанных с новостями
class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')  # Add ForeignKey
    image = models.ImageField(upload_to="news_images/")

    def __str__(self):
        return f"Image for {self.news.title}"
    


# Модель для категории (синяя часть на скриншоте)
class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

# Модель для сервиса (красная часть на скриншоте)
class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')  # Связь с категорией
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to="services_images/") 
    link = models.URLField(max_length=255) 

    def __str__(self):
        return self.name










# Модель для категории плантации (синяя часть на скриншоте)
class PlantationCategory(models.Model):
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name



class Plantation(models.Model):
    FRUIT_TYPES = (
        (1, 'Apple'),
        (2, 'Peach'),
    )

    name = models.CharField(max_length=50)
    INN = models.IntegerField()
    producer = models.CharField(max_length=255)

    garden_type = models.ForeignKey(PlantationCategory, on_delete=models.CASCADE, related_name='plantations_garden_type')
    fruit_type = models.IntegerField(choices=FRUIT_TYPES)
    
    category = models.ForeignKey(PlantationCategory, on_delete=models.CASCADE, related_name='plantations_category')
    # established_date = models.DateField()

    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='plantations')
    address = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    planting_scheme = models.CharField(max_length=20)
    garden_area = models.FloatField()
    irrigation_type = models.IntegerField()
    productivity = models.FloatField()
    tree_count = models.IntegerField()

    status = models.CharField(
        max_length=7,  # Максимальная длина наибольшего статуса ('yahshi' - 6 символов)
        choices=HealthStatus.choices,
        default=HealthStatus.YAHSHI  # По умолчанию статус 'Yahshi'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Plantation by {self.producer}'















# Модель для уведомлений
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Notification for {self.user.email}'

#! Модель для токенов сброса пароля
# class PasswordResetToken(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_tokens')
#     token = models.CharField(max_length=6)  # Простой токен в виде числового кода
#     expires_at = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Token for {self.user.email}'

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Модель пользователя
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=30, choices=[
        ('manufacturer', 'Manufacturer'),
        ('specialist', 'Specialist'),
        ('general_user', 'General User'),
        ('press_officer', 'Press Officer'),
        ('department_specialist', 'Department Specialist'),
        ('admin', 'Admin')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
