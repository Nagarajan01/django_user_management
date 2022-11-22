from django.urls import path
from .views import RegistrationView, LoginView, LogoutView,ChangePasswordView, UserList, Product_List, Cart
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(    
    'UserList', UserList
)
router.register(
    'Product_List', Product_List
)
router.register(
    'Product_List', Product_List
)
router.register(
    'Cart_List', Cart
)


app_name = 'users'

urlpatterns = [
    path('accounts/register', RegistrationView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='register'),
    path('accounts/logout', LogoutView.as_view(), name='register'),
    path('accounts/change-password', ChangePasswordView.as_view(), name='register'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls

