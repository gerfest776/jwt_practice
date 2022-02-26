from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from describe.views import InsultView

router = DefaultRouter(trailing_slash=False)
router.register('insult', viewset=InsultView)

urlpatterns = []
urlpatterns += router.urls
