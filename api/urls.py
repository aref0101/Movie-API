from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router= DefaultRouter()
router.register(r'movies', views.MovieViewSet)

urlpatterns= [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', views.RegisterGenerics.as_view()),
    path('bookmarks/', views.BookmarkAPIView.as_view()),
]