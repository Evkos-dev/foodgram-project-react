import json
import tempfile
from http import HTTPStatus

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from recipes.models import Favorite, Recipe, User
from rest_framework.test import (APIClient, APIRequestFactory, APITestCase,
                                 force_authenticate)

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


class ApiTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='user1')
        cls.guest_client = APIClient()
        cls.authorized_client = APIClient()
        cls.authorized_client.force_authenticate(
            cls.user,
        )
        cls.recipe = Recipe.objects.create(
            author=cls.user,
            name='recipe',
            text='test text',
            cooking_time='1',
        )

    # def test_favorite(self):
    #     response = self.authorized_client.post(
    #         reverse(
    #             'favorites-list',
    #             kwargs={'recipe_id': self.recipe.id}
    #         ),
    #         {"in_favorite": True},
    #         format='json'
    #     )
    #     self.assertEqual(HTTPStatus.OK, response.status_code)

    # def test_create_user(self):
    #     response = self.guest_client.get(
    #         reverse(
    #             'users-list'
    #         )
    #     )
    #     self.assertEqual(HTTPStatus.OK, response.status_code)




# class FavoriteTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='user1')
#         self.user2 = User.objects.create(username='user2')
#         self.recipe = Recipe.objects.create(
#             author=self.user,
#             name='recipe',
#             text='123',
#             cooking_time='1'
#         )

#     def test_favorite(self):
#         url = reverse('favorites-list', args=(self.recipe.id,))
#         data = {
#             "in_favorite": True,
#         }
#         json_data = json.dumps(data)
#         self.client.force_login(self.user2)
#         response = self.client.post(
#             url,
#             data=json_data,
#             content_type='application/json'
#         )
#         self.assertEqual(HTTPStatus.OK, response.status_code)
#         favorite = Favorite.objects.get(
#             user=self.user,
#             recipe=self.recipe
#         )
#         self.assertTrue(favorite.in_favorite)
