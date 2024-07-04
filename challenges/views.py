            # Author     : Sanjaykumar.M
            # Date       : 04-06-2024
            # Description: Django basic views and urls some example


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# def index(request):
#     return HttpResponse("This works!")

# def month(request):
#     return HttpResponse("THis is february")  
monthly_challenges = {
    "january": "1st month january!- sanjaykumar",
    "february": "2nd month february!- sanjaykumar",
    "march": "3rd month march!- sanjaykumar",
    "april": "4th month april!- sanjaykumar",
    "may": "5th month may!- sanjaykumar",
    "june": "6th month june!- sanjaykumar",
    "july": "7th month july!- sanjaykumar",
    "august": "8th month august!- sanjaykumar",
    "septemper": "9th month septemper!- sanjaykumar",
    "october": "10th month october!- sanjaykumar",
    "november": "11th month november!- sanjaykumar",
    "december": "12th month december!- sanjaykumar"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized}</a></li>"
    
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("this is invalid month")
     
    redirect_month = months[month-1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def month_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
        
    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")