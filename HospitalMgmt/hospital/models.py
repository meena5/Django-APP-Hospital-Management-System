from django.db import models


# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile_no=models.IntegerField()
    specialization=models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Patient(models.Model):
    name=models.CharField(max_length=50)
    mobile_no=models.IntegerField(null=True)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    issue=models.CharField(max_length=50)
    joining_date=models.DateTimeField(null=True)
    

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1=models.DateField(null=True)
    time1=models.TimeField()
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name


class Beds(models.Model):
    type=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    
    def __str__(self):
        return self.type