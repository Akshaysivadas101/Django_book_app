from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return '{}'.format(self.name)





class Book(models.Model):
    title = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)
    image= models.ImageField(upload_to='book_media',null=True)
    quantity= models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{}'.format(self.title)



