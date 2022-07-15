from signal import default_int_handler
from django.db import models


class Country(models.Model):
    class Meta:
        verbose_name_plural = "countries"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Roastery(models.Model):
    class Meta:
        verbose_name_plural = "roasteries"
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Variety(models.Model):
    class Meta:
        verbose_name_plural = "varieties"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Processing(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class Coffee(models.Model):
    roastery = models.ForeignKey(Roastery, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=None, blank=True, null=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=None, blank=True, null=True)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, default=None, blank=True, null=True)
    processing = models.ForeignKey(Processing, on_delete=models.CASCADE, default=None, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None, blank=True, null=True)
    elevation = models.CharField(max_length=100, default=None, blank=True, null=True)
    roast_date = models.DateTimeField('Date roasted', default=None, blank=True, null=True)
    on_the_shelf = models.BooleanField(default=True)
    coffee_image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.roastery.name} - {self.country.name}'
