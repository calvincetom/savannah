from rest_framework.routers import DefaultRouter
from orders.views import CustomerViewSet, OrderViewSet

# bind routes
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls