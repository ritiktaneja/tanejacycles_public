from django.db import models

# Create your models here.
from django.db import models

from .constants import Speed,Size,OrderStatus
import os
from uuid import uuid4
# Create your models here.


def path_and_rename(instance,filename):
        ext = filename.split('.')[-1]
        idd = '{}.{}'.format(uuid4().hex, ext)
        filename = instance.name +"-"+ idd
        path = 'bicycles' + '/'+ instance.brand.name
        return os.path.join(path,filename)
 

class Color(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    desc = models.CharField(max_length=1000)
    logo = models.ImageField(blank=True,upload_to='brand_logos/',max_length=None)

    def __str__(self):
        return self.name


class Bicycle(models.Model):
    name=models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="Bicycle")
    brand=models.ForeignKey(Brand, on_delete=models.SET_DEFAULT, default="",blank=True)
    #wheel_size=models.ForeignKey(Size,on_delete=models.SET_DEFAULT, db_column='size', default="Free Size")
    wheel_size=models.CharField(max_length=100,choices=[(i.name,i.value) for i in Size], default=Size.freesize.value)
    description=models.CharField(max_length=250)
    speed=models.CharField(max_length=100,choices=[(i.name,i.value) for i in Speed], default=Speed.speedsingle.value)
    #speed=models.ForeignKey(Speed,on_delete=models.SET_DEFAULT,default="Single Speed",null=True)
    color=models.ManyToManyField("Color")
    mrp=models.DecimalField(default=0, max_digits=10, decimal_places=2)
    price=models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    featured = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)

    image1=models.ImageField(blank=True,upload_to=path_and_rename, max_length=None)
    image2=models.ImageField(blank=True,upload_to=path_and_rename, max_length=None)
    image3=models.ImageField(blank=True,upload_to=path_and_rename, max_length=None)

    frame=models.CharField(blank=True,max_length=50)
    fork=models.CharField(blank=True,max_length=50)
    frame_material=models.CharField(blank=True,max_length=50)
    saddle=models.CharField(blank=True,max_length=50)
    rims=models.CharField(blank=True,max_length=50)
    gender=models.CharField(blank=True,max_length=50)
    brakes=models.CharField(blank=True,max_length=50)


    def __str__(self):
        stock = ""
        if self.in_stock:
            stock="IN STOCK"
        else :
            stock = "out of stock"

        return self.name + ' - ' + self.brand.name + '- Rs' + str(self.price) + " - " + stock
class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=100)
    addr2 = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100,blank=True,null=True)
    phone2 = models.CharField(max_length=15,blank=True,null=True)
    
    orderStatus = models.CharField(max_length=15,choices=[(i.name,i.value) for i in OrderStatus],default=OrderStatus.initiated.value)

    amount = models.DecimalField(max_digits=10,decimal_places=2)
    paymentStatus = models.CharField(max_length=15,default='Pending')
    paymentMethod = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=60,blank=True,null=True)
    payment_transaction_id = models.CharField(max_length=60,blank=True,null=True)
    
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.orderStatus

class Transaction(models.Model):
    CURRENCY = models.CharField(max_length=250,blank=True,null=True)
    GATEWAYNAME = models.CharField(max_length=250,blank=True,null=True)
    RESPMSG = models.CharField(max_length=250,blank=True,null=True)
    BANKNAME = models.CharField(max_length=250,blank=True,null=True)
    PAYMENTMODE = models.CharField(max_length=250,blank=True,null=True)
    MID = models.CharField(max_length=250,blank=True,null=True)
    RESPCODE = models.CharField(max_length=250,blank=True,null=True)
    TXNID = models.CharField(max_length=250,blank=True,null=True)
    TXNAMOUNT = models.CharField(max_length=250,blank=True,null=True)
    ORDERID = models.CharField(max_length=250,blank=True,null=True)
    STATUS = models.CharField(max_length=250,blank=True,null=True)
    BANKTXNID = models.CharField(max_length=250,blank=True,null=True)
    TXNDATE = models.CharField(max_length=250,blank=True,null=True)
    CHECKSUMHASH = models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return  "Order ID : "+str(self.ORDERID)

class SubOrder(models.Model):
    bicycle = models.ForeignKey(Bicycle,on_delete=models.SET_DEFAULT,default="bicycle")
    qty = models.IntegerField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    color = models.ForeignKey(Color, on_delete=models.SET_DEFAULT,default="color")
    ORDERID = models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ORDERID.id)

class Error(models.Model):
    error = models.CharField(blank=True,max_length=1000)

