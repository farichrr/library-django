from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=100, blank=True, null=True)
    publication = models.DateField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'book'

    def __str__(self):
        return self.title