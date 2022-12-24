from django.urls import include, path
from users.views import FollowingViewSet, FollowViewSet
from rest_framework.routers import DefaultRouter


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
