from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
import json


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {"username": "testcase", "email": "test@localhost.app",
                "password": "some_strong_psw"}
        response = self.client.post("http://localhost:8000/Api/register", json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login(self):
        data = {"username": "testcase","password": "some_strong_psw"}
        self.user = User.objects.create_user(username="testcase",
                                             password="some_strong_psw",email="test@localhost.app")
        self.token = Token.objects.create(user=self.user)
        response = self.client.post("http://localhost:8000/Api/login", json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

