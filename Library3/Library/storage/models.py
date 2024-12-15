from django.db import models

class Articles(models.Model):
    title = models.CharField('Название книги', max_length=250)
    avtor = models.CharField('Ф.И.О автора',max_length=250)
    idnumber = models.CharField('Номер книги',max_length=250)
    vidan = models.CharField('Кому выдана',max_length=250)
    vrem = models.DateTimeField('Время выдачи')
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/storage/{self.id}'
 
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

 