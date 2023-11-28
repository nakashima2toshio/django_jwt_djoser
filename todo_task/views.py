from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticated

from todo_task.models import Task
from todo_task.forms import TaskForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


class CustomLoginView(LoginView):
    template_name = 'todo_task/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    # get_context_data(self, **kwargs)

    def get_success_url(self):
        return reverse('todo_task:task_list')


class CustomLogoutView(LogoutView):
    template_name = 'todo_task/logout.html'

    def get_next_page(self):
        return reverse_lazy('todo_task:login')


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo_task/task_list.html'
    # permission_classes = [IsAuthenticated, ]
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskIndexView(LoginRequiredMixin, TemplateView):
    model = Task
    template_name = 'todo_task/task_index.html'
    permission_classes = [IsAuthenticated, ]
    success_url = reverse_lazy('todo_task:task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'hello_message'
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    permission_classes = [IsAuthenticated, ]
    template_name = 'todo_task/task_create.html'
    success_url = reverse_lazy('todo_task:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    permission_classes = [IsAuthenticated, ]
    template_name = 'todo_task/task_detail.html'
    success_url = reverse_lazy('todo_task:task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    permission_classes = [IsAuthenticated, ]
    template_name = 'todo_task/task_update.html'
    success_url = reverse_lazy('todo_task:task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo_task/task_confirm_delete.html'
    permission_classes = [IsAuthenticated, ]
    success_url = reverse_lazy('todo_task:task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskAboutView(LoginRequiredMixin, TemplateView):
    model = Task
    template_name = 'todo_task/task_about.html'
    # permission_classes = [IsAuthenticated, ]
    success_url = reverse_lazy('todo_task:task_list')
