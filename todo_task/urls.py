from django.urls import path

# from todo_task import api_views
from todo_task.views import CustomLoginView, TaskIndexView
from todo_task.views import CustomLogoutView
from todo_task.views import TaskAboutView
from todo_task.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

app_name = 'todo_task'

urlpatterns = [
    path('', TaskIndexView.as_view(), name='task_index'),
    path('list', TaskListView.as_view(), name='task_list'),
    path('about', TaskAboutView.as_view(), name='task_about'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    # path('api/tasks/', api_views.TaskListCreateAPIView.as_view(), name='task_api_list_create'),
    # path('api/tasks/<int:pk>/', api_views.TaskRetrieveUpdateDestroyAPIView.as_view(),
    # name='task_api_retrieve_update_destroy'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
