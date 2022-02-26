from rest_framework.routers import DefaultRouter

from auth_test.views import RegisterView

router = DefaultRouter(trailing_slash=False)
router.register('register', viewset=RegisterView)

urlpatterns = []
urlpatterns += router.urls
