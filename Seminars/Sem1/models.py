from django.db import models


class Coin(models.Model):
    toss = models.CharField(max_length=30)
    time = models.TimeField()

    def _str_(self):
        return f'{self.toss} at {self.time}'

    @staticmethod
    def coinstat(n: int):
        check = Coin.objects.order_by('-time')[:n]
        stats = {'heads': 0, 'tails': 0}
        for throw in check:
            if throw.toss == 'heads':
                stats['heads'] += 1
            else:
                stats['tails'] += 1
        return stats


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    biography = models.TextField(blank=True)
    birthdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Author - {self.surname} {self.name}'


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default='Risky Johny')
    view = models.IntegerField(default=0)
    is_publ = models.BooleanField(default=False)

    def __str__(self):
        return f'Article - {self.name} {self.body}'


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='product_photos/')

