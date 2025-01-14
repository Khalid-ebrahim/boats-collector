from django.db import models
from datetime import date
# Create your models here.

CHECKS = (
    ('one', 'CheckOne'),
    ('two', 'CheckTwo'),
    ('three', 'CheckThree')
)

class Boat(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField()
    description = models.TextField(max_length=250)
    production = models.CharField(max_length=100)
    # image = models.CharField(default=None, blank=True, null=True, max_length=2000)
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')

    def serves_for_today(self):
        return self.servicing_set.filter(date=date.today()).count() >= len(CHECKS)


class Servicing(models.Model):
    date = models.DateField()
    checks = models.CharField(max_length=6, choices=CHECKS, default=CHECKS[0][0])
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.boat} {self.get_checks_display()} on {self.date}"
