from api.pagination import CustomPagination
from djoser.views import UserViewSet
from rest_framework import status, views
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from users.models import Follow, User
from users.serializers import CustomUserSerializer, FollowingSerializer


class CustomUserViewSet(UserViewSet):
    """
    ViewSet для работы с пользователями.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FollowViewSet(views.APIView):
    """
    APIView для добавления и удаления подписки на автора.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def post(self, request, user_id):
        following = get_object_or_404(User, id=user_id)
        user = self.request.user
        Follow.objects.create(
            user=user,
            following=following
        )
        return Response(
            self.serializer_class(
                following,
                context={'request': request}
            ).data,
            status=status.HTTP_201_CREATED
        )

    def delete(self, request, user_id):
        following = get_object_or_404(User, id=user_id)
        user = self.request.user
        subscription = get_object_or_404(
            Follow,
            user=user,
            following=following
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowingView(ListAPIView):
    """
    APIView для просмотра подписок.
    """
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()
