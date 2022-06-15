from django.db import models

class rating(models.Model):
    image = models.ImageField('Картинка', upload_to='img/', default='main/static/main/img/kitigawa.png')
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL')
    description = models.TextField('Описание')
    year = models.IntegerField('Год')
    rating = models.IntegerField('Оценка', choices= [
                                                (1, '1/10'),
                                                (2, '2/10'),
                                                (3, '3/10'),
                                                (4, '4/10'),
                                                (5, '5/10'),
                                                (6, '6/10'),
                                                (7, '7/10'),
                                                (8, '8/10'),
                                                (9, '9/10'),
                                                (10, '10/10')
                                                     ])

    def __str__(self):
        return self.title
