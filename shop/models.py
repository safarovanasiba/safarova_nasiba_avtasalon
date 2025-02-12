from django.db import models
from datetime import datetime
# Create your models here.


class CarName(models.Model):
    title = models.CharField(max_length=255, verbose_name='Avtomobil nomi')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategory',
        verbose_name='Avtomobil turi')

    def __str__(self):
        return self.title


class CarLocation(models.Model):
    title = models.CharField(max_length=255, verbose_name='Viloyat nomi')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategory',
        verbose_name='Tuman yoki shahar nomi')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Shahar: pk={self.pk}, title={self.title}"


class CarsModel(models.Model):

    name = models.ForeignKey(CarName, on_delete=models.CASCADE, verbose_name='Avtomobil nomi')
    colour = models.CharField(max_length=255, choices=[
        ('white', 'white'),
        ('black', 'black')
    ])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sanasi")
    prise = models.CharField(max_length=255, verbose_name='Narxi')
    location = models.ForeignKey(CarLocation, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=[
                                  ('good', 'good'),
                                  ('excellent', 'excellent'),
                                  ('great', 'great')
                              ], verbose_name="Holati")

    distance = models.CharField(max_length=255, verbose_name='Masofaa yurgani')
    produced_at = models.IntegerField(choices=[(year, year) for year in range(1900, datetime.now().year)], verbose_name="Ishlab chiqarilgan yili")


    def get_first_photo(self):
        if self.images:
            try:
                return self.images.all()[0].image.url
            except:
                return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5igFUHiY5DMEZEKlymdVHp4r3MA9Pj7mEI6uKW_iT6A&s'
        return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5igFUHiY5DMEZEKlymdVHp4r3MA9Pj7mEI6uKW_iT6A&s'

    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'


class Gallery(models.Model):
    image = models.ImageField(upload_to='img/products/', verbose_name='Rasm')
    product = models.ForeignKey(CarsModel, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Rasmi'
        verbose_name_plural = 'Rasmlari'

