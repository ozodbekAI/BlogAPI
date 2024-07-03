from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tag', TagViewSet)
router.register(r'likedis', LikeOrDislikeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'', PostViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls