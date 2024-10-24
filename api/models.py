from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




#!UTILS:

HEALTH_STATUS = [
    ('yahshi', 'Yahshi'),
    ('ortacha', 'ortacha'),
    ('yomon', 'yomon'),
]
REGIONS = [
    ('tashkent_city', 'Tashkent City'),
    ('tashkent', 'Tashkent'),
    ('samarkand', 'Samarkand'),
    ('bukhara', 'Bukhara'),
    ('navoi', 'Navoi'),
    ('fergana', 'Fergana'),
    ('andijan', 'Andijan'),
    ('namangan', 'Namangan'),
    ('surkhandarya', 'Surkhandarya'),
    ('kashkadarya', 'Kashkadarya'),
    ('khorezm', 'Khorezm'),
    ('karakalpakstan', 'Karakalpakstan'),
    ('jizzakh', 'Jizzakh'),
    ('sirdarya', 'Sirdarya'),
]

# Словарь районов, привязанный к каждому региону
DISTRICTS = {
    'tashkent_city': [
        ('mirzo_ulugbek', 'Mirzo Ulugbek'),
        ('yakkasaray', 'Yakkasaray'),
    ],
    'tashkent': [
        ('bekabad', 'Bekabad'),
        ('chinaz', 'Chinaz'),
    ],
    'samarkand': [
              ('bulungur', 'Bulungur'),
        ('pakhtachi', 'Pakhtachi'),
    ],
    'bukhara': [
              ('buxara-1', 'buxara-1'),
    ],
    'navoi': [
              ('Navoi-1', 'Navoi-1'),
    ],
    'fergana': [
              ('Fergana-1', 'Fergana-1'),
    ],
    'andijan': [
              ('Andijan-1', 'Andijan-1'),
    ],
    'namangan': [
              ('Namangan-1', 'Namangan-1'),
    ],
    'surkhandarya': [
              ('Surkhandarya-1', 'Surkhandarya-1'),
    ],
    'kashkadarya': [
              ('Kashkadarya-1', 'Kashkadarya-1'),
    ],
    'khorezm': [
              ('Khorezm-1', 'Khorezm-1'),
    ],
    'karakalpakstan': [
              ('Karakalpakstan-1', 'Karakalpakstan-1'),
    ],
    'jizzakh': [
              ('zaamin', 'Zaamin'),
    ],
    'sirdarya': [
              ('gulistan', 'Gulistan'),
    ],
}





#?-----------------------------MODELS----------------------------------------
# Пользовательский менеджер для модели User
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


# Модель для плантаций
class Plantation(models.Model):
    name = models.CharField(max_length=50)
    producer = models.CharField(max_length=255)
    producer_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plantations_profile',blank=True,null=True)
    INN = models.IntegerField()
    established_date = models.DateField()
    category = models.ForeignKey(PlantationCategory,on_delete=models.CASCADE)

    latitude = models.CharField(max_length=255) 
    longitude = models.CharField(max_length=255) 
    address = models.CharField(max_length=255)
    area_size = models.FloatField()  

    crop_type = models.CharField(max_length=100)

    region = models.CharField(max_length=50, choices=REGIONS)
    district = models.CharField(max_length=50) 

    status = models.CharField(max_length=50, choices=HEALTH_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Plantation by {self.producer}'

    def get_district_choices(self):
        return DISTRICTS.get(self.region, [])















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