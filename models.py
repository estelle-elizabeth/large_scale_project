from django.db import models

# Create your models here.
class user(models.Model):
    #this will be populated whenever you have a new order
    user_id =  models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    order = models.BooleanField()

    def __str__ (self):
        return self.username

    # method for when user makes an order
    # needs to make rpc call
    # also needs to notify the truck to start its method

    # method for status update
    # changes the order_status to true which activates truck


class truck(models.Model):
    #customer = models.ForeignKey(user, on_delete=models.CASCADE)
    truck_id = models.CharField(max_length=50)
    menu = models.CharField(max_length=50)
    order_recieved = models.BooleanField()
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return self.truck_id
    # method to keep track of menu status
    # and send it using rpc automatically

class user_truck(models.Model):
    user_id = models.IntegerField(default=0)
    #truck_id = models.CharField(max_length=50)



#class menu(models.Model):
    #food_truck = models.ForeignKey(truck, on_delete=models.CASCADE)
    #menu = models.CharField(max_length=50)
