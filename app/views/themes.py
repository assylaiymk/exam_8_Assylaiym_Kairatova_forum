from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from app.forms import ThemeForm
from app.models import Theme


class ThemeCreate(LoginRequiredMixin, CreateView):
    template_name = 'theme_create.html'
    form_class = ThemeForm
    model = Theme

    def get_success_url(self):
        return reverse('theme_detail', kwargs={'pk': self.object.pk})


class ThemeView(DetailView):
    template_name = 'theme.html'
    model = Theme


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ThemeUpdateView(GroupPermission, LoginRequiredMixin, UpdateView):
    template_name = 'theme_update.html'
    form_class = ThemeForm
    model = Theme
    context_object_name = 'theme'
    groups = ['user', 'admin']

    def get_success_url(self):
        return reverse('theme_detail', kwargs={'pk': self.object.pk})


class ThemeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'theme_confirm_delete.html'
    model = Theme
    success_url = reverse_lazy('index')
