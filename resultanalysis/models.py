from django.db import models
from django.conf import settings


class batches(models.Model):
    choice=(('cse','cse'),('eee','eee'),('ece','ece'),('aero','aero'))
    batch_name=models.CharField(max_length=30,blank=True,default='not specified')
    batch_year_id=models.IntegerField(default=0)
    starting_year=models.CharField(max_length=30)
    ending_year=models.CharField(max_length=30)
    department=models.CharField(max_length=20,choices=choice,blank=True)
    college=models.CharField(max_length=50,blank=True,default='not specified')
    description=models.TextField(blank=True,default='not specified')
    thumb=models.ImageField(default='default.jpg',blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.batch_name

class excel_raw_data(models.Model):
    batch_name=models.CharField(max_length=30,blank=True)
    batch_id=models.IntegerField(default=1)
    sem_id=models.IntegerField(default=1)
    excel_data=models.FileField()

    def __str__(self):
        return '%s%s'%(self.batch_name,self.sem_id)

class arrears_excel_data(models.Model):
    batch_name=models.CharField(max_length=30,blank=True)
    batch_id=models.IntegerField(default=1)
    sem_id=models.IntegerField(default=1)
    arrear_sem_id=models.IntegerField(default=1)
    excel_data=models.FileField()

    def __str__(self):
        return '%s%s%s'%(self.batch_name,self.sem_id,self.arrear_sem_id)


class reevalutation_data(models.Model):
    batch_name=models.CharField(max_length=30,blank=True)
    batch_id=models.IntegerField(default=1)
    sem_id=models.IntegerField(default=1)
    excel_data=models.FileField()

    def __str__(self):
        return '%s%s'%(self.batch_name,self.sem_id)

class arrear_reevaluation_data(models.Model):
    batch_name=models.CharField(max_length=30,blank=True)
    batch_id=models.IntegerField(default=1)
    sem_id=models.IntegerField(default=1)
    arrear_sem_id=models.IntegerField(default=1)
    excel_data=models.FileField()
    
    def __str__(self):
        return '%s%s%s'%(self.batch_name,self.sem_id,self.arrear_sem_id)

class arrears_count_data(models.Model):
    batch_name=models.CharField(max_length=30,blank=True)
    batch_id=models.IntegerField(default=1)
    excel_data=models.FileField()

    def __str__(self):
        return '%s' %(self.batch_name)   

class came(models.Model):
     pdf_data=models.FileField()