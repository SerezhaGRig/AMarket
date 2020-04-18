from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=20, verbose_name="имя")
    count = models.IntegerField(null=True, blank=True, verbose_name="колич.")
    cost = models.FloatField(null=True, blank=True, verbose_name="цена")
    outdate = models.IntegerField(null=True, blank=True, verbose_name="Праср.(Шт)")
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    categ = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="категория")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="название")
    eng_name = models.CharField(max_length=20, db_index=True, verbose_name="name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категория'
        verbose_name = 'Категория'
        ordering = ['name']
