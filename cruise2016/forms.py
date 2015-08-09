from django import forms

class SignupForm(forms.Form):
    #basic
    name = forms.CharField(max_length=200)
    gender = forms.CharField(max_length=6)
    age = forms.CharField(max_length=2)
    phone = forms.CharField(max_length=200)
    email = forms.EmailField()
    person_type = forms.CharField(max_length=200)
    total_family_members = forms.CharField(max_length=2)

    #for exchange students
    #these don't need to be saved, just check that they are
    #checked before saving
    
    #host parent or parent name
    #only seen by children
    host_name = forms.CharField(max_length=200)
    host_phone = forms.CharField(max_length=200)
    host_email = forms.EmailField()

    #Shore Excursions
    #Cozumel
    excursion_1 = forms.CharField(max_length=200)
    #Belize
    excursion_2 = forms.CharField(max_length=200)
    #Mahogony Bay
    excursion_3 = forms.CharField(max_length=200)

    #ticks
    tick1 = forms.BooleanField()
    tick2 = forms.BooleanField()
    tick3 = forms.BooleanField()
    tick4 = forms.BooleanField()
    tick5 = forms.BooleanField()
    tick6 = forms.BooleanField()
    tick7 = forms.BooleanField()
    tick8 = forms.BooleanField()
    tick9 = forms.BooleanField()
    tick10 = forms.BooleanField()