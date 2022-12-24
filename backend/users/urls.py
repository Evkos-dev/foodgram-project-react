from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import FollowingViewSet, FollowViewSet

router = DefaultRouter()
router.register(r"subscriptions/", FollowingViewSet, basename="subscriptions")
router.register(
    r"(?P<user_id>\d+)/subscribe/",
    FollowViewSet,
    basename="subscribe"
)


urlpatterns = [
    path("", include(router.urls)),
    path("", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
]
