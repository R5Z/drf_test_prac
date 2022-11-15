from django.urls import reverse # url에 있는 네임값으로 테스트 가능. 향후 url이 바뀌더라도 네임값을 사용하기 때문에 오류가 나거나 꼬일 위험이 적다
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User, UserManager


class UserRegistrationTest(APITestCase): 
    def test_registration(self):
        url = reverse("userview")
        user_data = {
            "username": "testsign",
            "email": "te@st.com",
            "fullname": "rose",
            "password": "wkdal"
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.json(), {
            "message": "가입 완료!!"
        })