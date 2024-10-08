from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #Auth
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    #News
    path('news/', NewsListCreateView.as_view(), name='news-list-create'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('newsimages/', NewsIMages.as_view(), name='newsimages-list-create'),

    # Services
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'), 
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'), 
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'), 
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
]