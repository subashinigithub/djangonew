from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=255)
    age=models.PositiveIntegerField()
    salary=models.PositiveIntegerField()
    designation=models.CharField(max_length=255)
    experience=models.PositiveIntegerField()
    gender=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
"""
{
"name":"subashini",
"age":"23",
"salary":"30000",
"designation":"testing",
"experience":"2",
"gender":"female"

}
"""
