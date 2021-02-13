from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.TextField(blank=True, null=True)  # This field type is a guess.
    publication = models.DateField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'book'