from rest_framework.routers import DefaultRouter
from . import auth

router = DefaultRouter()
router.register(r'auth', auth.AuthViewSet, basename='auth')

urlpatterns = router.urls
