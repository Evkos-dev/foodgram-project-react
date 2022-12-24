from api.pagination import CustomPagination
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from users.serializers import FollowingSerializer, FollowSerializer


class CreateDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


# class CustomUserViewSet(UserViewSet):
#     queryset = User.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]


class FollowViewSet(CreateDestroyViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete(user=self.request.user)


class FollowingViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FollowingSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()
