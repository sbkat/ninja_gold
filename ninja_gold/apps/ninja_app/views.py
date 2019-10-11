from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random

def index(request):
    if "number_moves" not in request.session:
        request.session["number_moves"] = 0
    if "gold_goal" not in request.session:
        request.session["gold_goal"] = 0
    if "your_gold" not in request.session:
        request.session["your_gold"] = 0
    if "counter" not in request.session:
        request.session["counter"] = 0
    context = {
        "time": strftime("%B %d, %Y %I:%M %p", localtime())
    }
    return render(request, 'ninja_app/index.html', context)

def process(request, name):
    if name == 'farm':
        request.session["random_number"] = random.randint(10,20)
        request.session["your_gold"] += request.session["random_number"]
        request.session["location"] = 'farm'
        request.session["counter"] += 1
    if name == 'cave':
        request.session["random_number"] = random.randint(5,10)
        request.session["your_gold"] += request.session["random_number"]
        request.session["location"] = 'cave'
        request.session["counter"] += 1
    if name == 'house':
        request.session["random_number"] = random.randint(2,5)
        request.session["your_gold"] += request.session["random_number"]
        request.session["location"] = 'house'
        request.session["counter"] += 1
    if name == 'casino':
        request.session["random_number"] = random.randint(-50,50)
        request.session["random_number_neg"] = request.session["random_number"] * -1
        request.session["your_gold"] += request.session["random_number"]
        request.session["location"] = 'casino'
        request.session["counter"] += 1
    return redirect ('/')

def winning_conditions(request):
    if request.method == "POST":
        request.session["number_moves"] = int(request.POST["input1"])
        request.session["gold_goal"] = int(request.POST["input2"])

        print(request.session["number_moves"])
        print(request.session["gold_goal"])
    return redirect ('/')

def reset(request):
    request.session.clear()
    return redirect ('/')