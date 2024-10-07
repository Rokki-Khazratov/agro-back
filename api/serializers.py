from rest_framework import serializers
from core.settings import BASE_URL  
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'created_at']





# Сериализатор для изображений
class NewsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()  # Custom method for images
    category = serializers.SerializerMethodField()  # Custom method for images

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'category', 'images', 'created_at', 'updated_at']

    # Fetch images related to the news
    def get_images(self, obj):
        return [f"{BASE_URL}{image.image.url}" for image in obj.images.all()]

    def get_category(self, obj):
        return obj.category.name
    
    def create(self, validated_data):
        return News.objects.create(**validated_data)

class NewsImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField() 

    class Meta:
        model = NewsImage
        fields = ['image', 'news']  

    def create(self, validated_data):
        image = validated_data.pop('image')
        news = validated_data.pop('news')
        instance = NewsImage.objects.create(image=image, news=news)
        return instance