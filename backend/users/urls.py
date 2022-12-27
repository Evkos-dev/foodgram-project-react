from django.urls import include, path

from users.views import FollowingView, FollowViewSet

urlpatterns = [
    path(
        'users/subscriptions/',
        FollowingView.as_view(),
        name='subscriptions'
    ),
    path(
        'users/<int:user_id>/subscribe/',
        FollowViewSet.as_view(),
        name='subscribe'
    ),
    path("", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
]
