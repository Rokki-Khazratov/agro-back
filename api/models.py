from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




#!UTILS:







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

# Модель для новостей
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100)
    images = models.ManyToManyField('NewsImage', related_name='news_images', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Модель для хранения изображений, связанных с новостями
class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="news_images/")

    def __str__(self):
        return f"Image for {self.news.title}"

# Модель для продуктов
class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    producer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    harvest_time = models.DateField()

    forecast = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Модель для плантаций
class Plantation(models.Model):
    producer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plantations')
    location = models.CharField(max_length=255) 
    status = models.CharField(max_length=50)
    established_date = models.DateField()
    area_size = models.FloatField()  
    crop_type = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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