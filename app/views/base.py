from urllib.parse import urlencode

from django.db.models import Q
from django.views.generic import ListView
from app.models import Theme
from app.forms import SearchForm


class IndexView(ListView):
    template_name = 'index.html'
    model = Theme
    context_object_name = 'themes'
    ordering = ('-created_at',)
    paginate_by = 4
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['themes'] = Theme.objects.filter(is_deleted=False)
        return context

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_from()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_from(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context
