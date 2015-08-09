from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm
from django.utils import timezone
from cruise2016.models import SignUp


## VIEWS

#front page
def index(request):
    return render(request, 'cruise2016/index.html')

#sign up for 2016 cruise
def signup(request):
    #ad hoc function for cleaning post_data
    def remove_ticks(x):
        #pop list
        remove = ["tick1", "tick2", "tick3", "tick4", "tick5", "tick6", "tick7", "tick8", "tick9", "tick10"]
    
        #pop
        for i in remove:
            x.pop(i, None)

        #return
        return(x)

    #save post data
    if request.method == 'POST':
        form = SignupForm(request.POST)

        #check validity of input
        #this also cleans the data input
        valid = form.is_valid()
        
        #check validity depending on person_type
        post_data = form.cleaned_data

        #calculate price
        price_list = {"Stay on ship": 0,
        "Stand-up Paddle Boarding, Snorkel and Beach": 60,
        "Ancient Culture / Mayan Ruins & Beach": 70,
        "Dark Knight Cave Tubing": 80,
        "Sergeant's Cay Snorkel Adventure": 80,
        "Relax on the Beach": 20,
        "Zip-Line Express": 60}
        price = 450 + price_list[post_data["excursion_1"]] + price_list[post_data["excursion_2"]] + price_list[post_data["excursion_3"]]

        #did user provide the type?
        if not "person_type" in post_data:
            #send them back
            print("User did not provide person_type")
            return render(request, 'cruise2016/signup.html', post_data)

        #exchange students
        if post_data["person_type"] == "Exchange student":
            #this is the list of required forms
            req = set(["name", "gender", "age", "phone", "email", "total_family_members", "host_name", "host_phone", "host_email", "excursion_1", "excursion_2", "excursion_3", "tick1", "tick2", "tick3", "tick4", "tick5", "tick6", "tick7", "tick8", "tick9", "tick10"])
            #find the set of non-provided but required forms
            needed = req - set(post_data)

            if set() == needed: #check that none are missing, i.e. missing must be empty set
                #remove unused entries in dict
                post_data = remove_ticks(post_data)

                #save to database
                s = SignUp(signup_date = timezone.now(), price = price, **post_data)
                s.save()
                return HttpResponse("Thanks for signing up!")
            else:
                print("not all fields were filled out for exchange student")
                print(needed)
        #repeat same setup for host sibling and host parent, with different requirements

        #host siblings
        if post_data["person_type"] == "Host sibling":
            req = set(["name", "gender", "age", "phone", "email", "total_family_members", "host_name", "host_phone", "host_email", "excursion_1", "excursion_2", "excursion_3"])
            needed = req - set(post_data)

            if set() == needed:
                #remove unused entries in dict
                post_data = remove_ticks(post_data)

                s = SignUp(signup_date = timezone.now(), price = price, **post_data)
                s.save()
                return HttpResponse("Thanks for signing up!")
            else:
                print("not all fields were filled out for host sibling")
                print(needed)

        #host parents
        if post_data["person_type"] == "Host parent":
            req = set(["name", "gender", "age", "phone", "email", "total_family_members", "excursion_1", "excursion_2", "excursion_3"])
            needed = req - set(post_data)
            if set() == needed:
                #remove unused entries in dict
                post_data = remove_ticks(post_data)

                s = SignUp(signup_date = timezone.now(), price = price, **post_data)
                s.save()
                return HttpResponse("Thanks for signing up!")
            else:
                print("not all fields were filled out for host parent")
                print(needed)


        #else
        return render(request, 'cruise2016/signup.html', post_data)

    else:
        #did not submit the forms, show forms (i.e. on first load or non-send refresh)
        return render(request, 'cruise2016/signup.html')
