from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from app.forms import ReplyForm
from app.models import Reply


class ReplyCreate(LoginRequiredMixin, CreateView):
    template_name = 'reply_create.html'
    form_class = ReplyForm
    model = Reply

    def get_success_url(self):
        return reverse('reply_detail', kwargs={'pk': self.object.pk})


class ReplyView(DetailView):
    template_name = 'reply.html'
    model = Reply


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ReplyUpdateView(GroupPermission, LoginRequiredMixin, UpdateView):
    template_name = 'reply_update.html'
    form_class = ReplyForm
    model = Reply
    context_object_name = 'reply'
    groups = ['user', 'admin']

    def get_success_url(self):
        return reverse('reply_detail', kwargs={'pk': self.object.pk})


# class ThemeDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = 'theme_confirm_delete.html'
#     model = Theme
#     success_url = reverse_lazy('index')
