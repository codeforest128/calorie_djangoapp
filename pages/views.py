from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import CalorieData


class HomePageView(TemplateView):
    template_name = 'home.html'

# class MainPageView(TemplateView):
#     template_name = 'main.html'

@login_required

def index(request):
    # return HttpResponse("Hello,world. You're at the polls index.")
    calorie_list = CalorieData.objects.all()
    return render(request, "main.html", {'caloriedata':calorie_list})
# Create your views here.


def save(request):
    if request.POST:
        print(request.POST)
        calorie = CalorieData()
        calorie.calorie = request.POST['totalcalorie']
        calorie.pub_date = request.POST['pubdate']
        calorie.save()
    return redirect('/main/')

def delete(request,caloriedata_id = None):
    object = CalorieData.objects.get(id=caloriedata_id)
    object.delete()
    return redirect('/main/')