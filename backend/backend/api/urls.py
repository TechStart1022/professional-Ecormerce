from django.urls import path
from userauths import views as userauths_views


from store import views as stroe_views

urlpatterns = [
    path('user/token/',userauths_views.TokenObtainPairView.as_view())
]