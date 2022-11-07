from django.db import models

# Create your models here.

#BookNumber Table Data (one book has one number)
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=10, blank=True)
    

#Book main table data   
class Book(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    #one to one relation
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)
    
    #show the table in title name
    def __str__(self) -> str:
        return self.title
    
#Character table data (one book has many character) && has set a foreignkey(main table) && one to many (related_name='')
class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

#Author table data (many to many) && many to many (related_name='')
class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='authors')
                                 
                                 
