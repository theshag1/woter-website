from django.db import models


class Travel(models.Model):
    title = models.CharField(max_length=250)
    deccraption = models.TextField()
    image = models.ImageField()
    day = models.IntegerField()
    documents = models.TextField()
    travelday = models.DateTimeField
    price = models.FloatField()
    farmname = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title


class Category(models.Model):

    FarmName = models.CharField(max_length=250)
    Image = models.ImageField()

    def __str__(self):
        return self.FarmName
