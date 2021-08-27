from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Author 


# We want an Author created for each new User

# We have a signal of (post_save) so...
# When a user is saved we send a signal which will be received by the (receiver = the AuthorCreateView Class)
@receiver(post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(name=instance)

# Just saves the profile each time the user object gets saved
@receiver(post_save, sender=User)
def save_author(sender, instance, **kwargs):
    instance.author.save()

