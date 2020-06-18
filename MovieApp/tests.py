from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from MovieApp.models import Movie
from rest_framework.test import APITestCase
import json


class MovieTestCase(APITestCase):

    def test_movieadd(self):
        data = {"movie": "Humtum"}
        self.user = User.objects.create_user(username="testcase",
                                             password="some_strong_psw", email="test@localhost.app")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post("http://localhost:8000/Movie/movieadd", json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rating(self):
        data = {"movie": "Humtum","rating":5}
        self.user = User.objects.create_user(username="testcase",
                                             password="some_strong_psw", email="test@localhost.app")
        Movie.objects.create(movie_name="Humtum",creator=self.user)
        self.user1 = User.objects.create_user(username="testcase1",
                                             password="some_strong_psw", email="test@localhost.app")
        self.token = Token.objects.create(user=self.user1)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post("http://localhost:8000/Movie/rater",json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,response)
