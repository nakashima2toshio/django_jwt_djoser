# views.pi
import logging

from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import views, status
from .serializers import UserSerializer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

User = get_user_model()


# 既存のUserListクラス
class UserList(ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


# 新しいユーザーを作成するためのクラス
class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # ここでユーザーの作成や追加のロジックを実装できます
        serializer.save()


class ActivateAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uid, token) -> Response:
        logger = logging.getLogger(__name__)
        # activation APIのURL
        url = "http://127.0.0.1:8000/api/auth/users/activation/"

        # リクエストのペイロードを設定
        payload = {'uid': uid, 'token': token}
        logger.error(f"UID: {uid}")
        logger.error(f"Token: {token}")

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, json=payload)
        # レスポンスのステータスコードを確認
        if response.status_code == 200:
            logger.info(f"Response: {response}")
            return Response({"message": "Activation successful OK!"}, status=status.HTTP_200_OK)
        else:
            logger.error(f"Response: {response}")
            return Response({"message": "Activation failed -------"}, status=status.HTTP_400_BAD_REQUEST)