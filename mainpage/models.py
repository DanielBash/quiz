from django.db import models


# Create your models here.
class Question(models.Model):
    number = models.TextField(blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    correct = models.TextField(blank=True)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'Вопрос'