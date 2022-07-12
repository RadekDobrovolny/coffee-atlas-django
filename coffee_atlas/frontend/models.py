from django.db import models


class Country(models.Model):
    class Meta:
        verbose_name_plural = "countries"
    name = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Roastery(models.Model):
    class Meta:
        verbose_name_plural = "roasteries"
    name = models.CharField(max_length=100, default='Unknown')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Variety(models.Model):
    class Meta:
        verbose_name_plural = "varieties"
    name = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name


class Processing(models.Model):
    name = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name


class Coffee(models.Model):
    roastery = models.ForeignKey(Roastery, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    processing = models.ForeignKey(Processing, on_delete=models.CASCADE)
    elevation = models.CharField(max_length=100)
    roast_date = models.DateTimeField('Date roasted')
    on_the_shelf = models.BooleanField(default=True)
