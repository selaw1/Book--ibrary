from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User

from .models import Author, Book


AuthorBooksFormset = inlineformset_factory(Author, Book, 
                                                    fields=('title',),
                                                    extra=2,
                                                    )

class AuthorFormSet(AuthorBooksFormset):
    def add_fields(self, form, index):
        super().add_fields(form,index)
        form.fields['title'].widget.attrs.update({'placeholder': 'Book Title'})
        form.fields['title'].label = ''

class AuthorCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self):
        user = super().save()
        author = Author.objects.create(name=user)
        author.save()
        return author
