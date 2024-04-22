from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import save_form_data



def home(request):
    return render(request,"index.html")


def save_data(request):
    n=''
    if request.method=="POST":
        EducationType = request.POST.get('educationType')
        EducationLevel = request.POST.get('educationLevel')
        Experience = request.POST.get('experience')
        data=save_form_data(education_type=EducationType,education_level=EducationLevel,years_of_experience=Experience)
        data.save()
        n='Data Saved'
    return render(request,"index.html",{'n':n})

