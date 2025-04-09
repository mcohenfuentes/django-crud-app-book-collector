from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

STATUSES = (
    ('S', 'Started'),
    ('P', 'In Progress'),
    ('F', 'Finished'),
    ('R', 'Re-read'),
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.id})
    
class Reading(models.Model):
    date = models.DateField('Current Reading Date')
    status = models.CharField(
        max_length=1,
        choices=STATUSES,
        default=STATUSES[0][0]
    )
    notes = models.TextField(max_length=250)

    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_status_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date'] 