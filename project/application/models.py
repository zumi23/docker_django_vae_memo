from django.db import models
from django.utils import timezone
import pytz
from django.urls import reverse_lazy
from django.dispatch import receiver
import os


class BaseModel(models.Model):
    create_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone('Asia/Tokyo')))
    update_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone('Asia/Tokyo')))

    class Meta:
        abstract = True


# class Books(BaseModel):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=1000)
#     price = models.IntegerField()

#     class Meta:
#         db_table = 'books'

#     def get_absolute_url(self):
#         return reverse_lazy('store:detail_book', kwargs={'pk': self.pk})


# class PicturesManager(models.Manager):
#     def filter_by_book(self, book):
#         return self.filter(book=book).all()


# class Pictures(BaseModel):

#     picture = models.FileField(upload_to='picture/')
#     book = models.ForeignKey(
#         'books', on_delete=models.CASCADE
#     )
#     objects = PicturesManager()


# @receiver(models.signals.post_delete, sender=Pictures)
# def delete_picture(sender, instance, **kwargs):
#     if instance.picture:
#         if os.path.isfile(instance.picture.path):
#             os.remove(instance.picture.path)


# class Pokemons(BaseModel):
#     # name_id = models.IntegerField()
#     type1_id = models.IntegerField()
#     type2_id = models.IntegerField()
#     egg1_id = models.IntegerField()
#     egg2_id = models.IntegerField()

#     class Meta:
#         db_table = 'pokemons'


# class Pokeinfos(BaseModel):
#     poke_id = models.ForeignKey('pokemons', on_delete=models.PROTECT)
#     name = models.CharField(max_length=20)
#     height = models.FloatField()
#     weight = models.FloatField()
#     img_path = models.CharField(max_length=200)

#     class Meta:
#         db_table = 'pokeinfos'


