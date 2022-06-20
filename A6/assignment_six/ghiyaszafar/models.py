from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
import os


# Create your models here.
class student(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    email = models.EmailField(blank=False, null=False, max_length=100)

    def __str__(self):
        return str(self.email)


class studentprofile(models.Model):
    profile = models.ImageField(blank=True, null=True, upload_to='images',default='img.png')
    username = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return str(self.username)

def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

@receiver(post_delete, sender = studentprofile)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.profile:
        _delete_file(instance.profile.path)
        print("You have just deleted something")


@receiver(pre_delete, sender=studentprofile)
def delete_img_pre_delete_post(sender, instance, *args, **kwargs):
    if instance.profile:
        _delete_file(instance.profile.path)
        print("you are about to delete something")