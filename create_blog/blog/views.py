from django.shortcuts import render, get_object_or_404
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
context_home = {
    "tasks": Task.objects.all()
}

context_about = {
    "title": "About"
}

def home(request):
    return render(request, "blog/home.html", context=context_home)

class TaskListView(ListView):
    model = Task
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "tasks"
    ordering = ['-task_created_date']
    paginate_by = 5

class UserTaskListView(ListView):
    model = Task
    template_name = "blog/user_task_list.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Task.objects.filter(author=user).order_by('-task_created_date')

class TaskDetailedView(DetailView):
    model = Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_name', 'task_description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['task_name', 'task_description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()

        if self.request.user == task.author:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = "/"

    def test_func(self):
        task = self.get_object()

        if self.request.user == task.author:
            return True
        return False

def about(request):
    return render(request, "blog/about.html", context=context_about)
