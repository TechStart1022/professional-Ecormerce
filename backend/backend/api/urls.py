from django.urls import path
from userauths import views as userauths_views
from rest_framework_simplejwt.views import TokenRefreshView

from store import views as stroe_views

urlpatterns = [
    path('user/token/refresh/',TokenRefreshView.as_view()),
    path('user/token/',userauths_views.TokenObtainPairView.as_view()),
    path('user/register/',userauths_views.RegisterView.as_view()),
    path('user/password-reset/<email>/',userauths_views.PasswordResetEmailVerify.as_view()),
    path('user/password-change/',userauths_views.PasswordChangeView.as_view()),

]