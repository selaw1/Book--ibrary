from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction

from .models import Book, Author
from .forms import AuthorFormSet, AuthorCreateForm


class HomeView(TemplateView):
    template_name = 'books/home.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_detail.html'

    # One way of getting all books for specific author
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     author = get_object_or_404(Author, id=self.kwargs.get('pk'))
    #     context['books'] = Book.objects.filter(author=author)
    #     print(author)
    #     return context


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'books/author_create.html'
    form_class = AuthorCreateForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Author Created Successfully!'
        ) 
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('books:login')

class AuthorBooksEditView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Author
    template_name = 'books/author_books_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return AuthorFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes Were Saved'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('books:author_detail', kwargs={'pk': self.object.pk})