from django.db import models


# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()

    class Meta:
        db_table = "Booking"

    def __str__(self):
        return self.Name


class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    class Meta:
        db_table = "Menu"

    def __str__(self):
        return f"{self.Title} : {str(self.Price)}"
