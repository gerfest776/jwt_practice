from rest_framework.routers import DefaultRouter

from describe.views import InsultView

router = DefaultRouter(trailing_slash=False)
router.register('insult', viewset=InsultView)

urlpatterns = []
urlpatterns += router.urls
