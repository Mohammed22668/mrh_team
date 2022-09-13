from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# from django.utils.translation import ungettext_lazy as _

# Create your models here.


class Category (models.Model):
    Cname=models.CharField(max_length=75,verbose_name="اسم الفئة")
    
    def __str__(self):
        return self.Cname
    
class Project(models.Model):
    Pname = models.CharField(max_length=75 , verbose_name="اسم المشروع")
    category = models.ForeignKey(Category,null=True,blank=True,verbose_name="الفئة" , on_delete=models.PROTECT)
    img1 = models.ImageField(
        upload_to='photos/%y/%m/%d', default='photos/%y/%m/%d')
    img2 = models.ImageField(
        upload_to='photos/%y/%m/%d', default='photos/%y/%m/%d')
    img3 = models.ImageField(
        upload_to='photos/%y/%m/%d', default='photos/%y/%m/%d')
    img4 = models.ImageField(
        upload_to='photos/%y/%m/%d', default='photos/%y/%m/%d')
    date_time = models.DateTimeField(default=datetime.now())
    detail = models.TextField(max_length=250, verbose_name="التفاصيل",  null=True, blank=True)
    
    def __str__(self):
        return self.Pname


class Rusul(models.Model):
    Rname=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="الاسم")
    Rprof = models.CharField(
        max_length=150, verbose_name="الاختصاص", blank=True)
    Rinfo = models.TextField(max_length=500,verbose_name="المعلومات",blank=True)
    Rimg = models.ImageField(upload_to="photos/%y/%m/%d",verbose_name="الصورة")
    
    
    def __str__(self):
        return str(self.Rname)
    

class Hussain(models.Model):
    Hname = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="الاسم")
    Hprof = models.CharField(
        max_length=150, verbose_name="الاختصاص", blank=True)
    Hinfo = models.TextField(
        max_length=500, verbose_name="المعلومات", blank=True)
    Himg = models.ImageField(
        upload_to="photos/%y/%m/%d", verbose_name="الصورة")

    def __str__(self):
        return str(self.Hname)


class Mohammed(models.Model):
    Mname = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="الاسم")
    Mprof = models.CharField(max_length=150, verbose_name="الاختصاص",blank=True)
    Minfo = models.TextField(
        max_length=500, verbose_name="المعلومات", blank=True)
    Mimg = models.ImageField(
        upload_to="photos/%y/%m/%d", verbose_name="الصورة")

    def __str__(self):
        return str(self.Mname)


class Members(models.Model):
    MMname = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="الاسم")
    MMfullname = models.CharField(max_length=150,
         verbose_name="الاسم الكامل",blank=True)    
    MMprof = models.CharField(
        max_length=150, verbose_name="الاختصاص", blank=True)
    MMinfo = models.TextField(
        max_length=500, verbose_name="المعلومات", blank=True)
    MMimg = models.ImageField(
        upload_to="photos/%y/%m/%d", verbose_name="الصورة")

    def __str__(self):
        return str(self.MMname)
    
    
class Posts(models.Model):
    Ptitle = models.CharField(max_length=100 , verbose_name="Title" )
    Pcategory = models.ForeignKey(Category,on_delete=models.CASCADE , verbose_name="Category")
    Pdetails = models.TextField(verbose_name="Details",null=True)
    Pimg = models.ImageField(upload_to="photos/%y/%m/%d" , verbose_name="Image")
    Pdata_time = models.DateTimeField(default=datetime.now())
    Pmember = models.ForeignKey(Members,on_delete=models.CASCADE,verbose_name="User")
    
    
    def __str__(self):
         return self.Ptitle

    
