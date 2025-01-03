from django.db import models
class Customer(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(unique=True)

    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=200)
    def isexit(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

