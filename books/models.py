from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name



class Books(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books/images/")
    author_name = models.CharField(max_length=255)
    published_date = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('books.Category', on_delete=models.CASCADE)
    star_rate = models.DecimalField(max_length=5 , decimal_places=0 , max_digits=1)
    is_deleted = models.BooleanField(default=False)

    def _str_(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Books List'
        verbose_name_plural = 'Books List'



class Comments(models.Model):
    text = models.TextField()
    book_name = models.ForeignKey('books.Books', on_delete=models.CASCADE)


    class Meta:
       verbose_name = 'Comment List'
       verbose_name_plural = 'Comments List'

    def __str__(self):
        return str(self.id)
      