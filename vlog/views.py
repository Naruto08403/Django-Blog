from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models import Prefetch
from .models import VlogPost
from .forms import VlogPostForm

# Create your views here.

class VlogListView(LoginRequiredMixin, ListView):
    model = VlogPost
    template_name = 'vlog/vlog_list.html'
    context_object_name = 'vlogs'
    paginate_by = 10
    ordering = ['-published_date']
    
    def get_queryset(self):
        return VlogPost.objects.select_related('author')

@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache for 15 minutes
class VlogDetailView(LoginRequiredMixin, DetailView):
    model = VlogPost
    template_name = 'vlog/vlog_detail.html'
    context_object_name = 'vlog'
    
    def get_queryset(self):
        return VlogPost.objects.select_related('author')

class VlogCreateView(LoginRequiredMixin, CreateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = 'vlog/vlog_form.html'
    success_url = reverse_lazy('vlog:vlog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VlogUpdateView(LoginRequiredMixin, UpdateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = 'vlog/vlog_form.html'
    success_url = reverse_lazy('vlog:vlog_list')

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

# Public views that don't require authentication
class PublicVlogListView(ListView):
    model = VlogPost
    template_name = 'vlog/public_vlog_list.html'
    context_object_name = 'vlogs'
    paginate_by = 10
    ordering = ['-published_date']

class PublicVlogDetailView(DetailView):
    model = VlogPost
    template_name = 'vlog/public_vlog_detail.html'
    context_object_name = 'vlog'
