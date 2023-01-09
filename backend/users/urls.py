from django.urls import include, path
from users.views import FollowingView, FollowViewSet

users_patterns = [
    path(
        'subscriptions/',
        FollowingView.as_view(),
        name='subscriptions'
    ),
    path(
        '<int:user_id>/subscribe/',
        FollowViewSet.as_view(),
        name='subscribe'
    ),
]

urlpatterns = [
    path('users/', include(users_patterns)),
    path("", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
]
