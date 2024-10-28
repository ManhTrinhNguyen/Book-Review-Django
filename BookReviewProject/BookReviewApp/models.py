from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  Genre = models.CharField(max_length=50)
  puplic_date = models.DateField()
  description = models.TextField(blank=True)

  def __str__(self):
    return self.title

class Review(models.Model):
  book = models.ForeignKey(Book, on_delete=models.PROTECT ,related_name='reviews')
  review_text = models.TextField()
  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  date_reviewed = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'Review for {self.book.title} by {self.book.author}'
  
  
