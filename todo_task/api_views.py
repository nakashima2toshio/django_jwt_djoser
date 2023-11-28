from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

"""
CRUD APIエンドポイント

GET /todo/api/tasks/: タスク一覧の取得
POST /todo/api/tasks/: 新規タスクの作成
GET /todo/api/tasks/<int:pk>/: タスクの詳細情報取得
PUT /todo/api/tasks/<int:pk>/: タスクの更新
PATCH /todo/api/tasks/<int:pk>/: タスクの部分的な更新
DELETE /todo/api/tasks/<int:pk>/: タスクの削除
"""


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
