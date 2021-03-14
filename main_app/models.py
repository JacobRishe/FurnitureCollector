from django.db import models
# from django.contrib.auth.models import User

# constant variable
SUPPLIES = (
     ('S', 'Sledge hammer'),
     ('B', 'Bat'),
     ('C', 'Chainsaw')
)



# Create your models here.


class Furniture(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Destroy(models.Model):
    date = models.DateField("Destroy Date")
    supply = models.CharField(
        "Pick Your Destroy Object!",
        max_length=1,
        choices=SUPPLIES,
        default=SUPPLIES[0][0]
    )
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_supply_display()} on {self.date}"

    class Meta:
        ordering = ['-date']









#just after toys
# user = models.ForeignKey(User, on_delete=models.CASCADE)
