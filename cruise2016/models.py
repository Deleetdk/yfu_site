from django.db import models

#the sign up table
class SignUp(models.Model):
    #primary key
    id = models.AutoField(primary_key=True)

    #basic
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6)
    age = models.CharField(max_length=2)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    person_type = models.CharField(max_length=200)
    total_family_members = models.CharField(max_length=2)

    #for exchange students
    #these don't need to be saved, just check that they are
    #checked before saving
    
    #host parent or parent name
    host_name = models.CharField(max_length=200, null = True)
    host_phone = models.CharField(max_length=200, null = True)
    host_email = models.EmailField(null = True)

    #Shore Excursions
    #Cozumel
    excursion_1 = models.CharField(max_length=200)
    #Belize
    excursion_2 = models.CharField(max_length=200)
    #Mahogony Bay
    excursion_3 = models.CharField(max_length=200)
    
    #price
    price = models.IntegerField()

    #payment
    #this is changed manually by the trip arranger
    paid = models.BooleanField(default=False)

    #date
    #set to the set the form was sent
    signup_date = models.DateTimeField()

    #make for better output
    def __str__(self): 
        return self.name