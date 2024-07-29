from django.db import models
class employee(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    email=models.EmailField()

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)


 