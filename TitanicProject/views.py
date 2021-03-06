# File to store functions
from django.shortcuts import render
from . import test_model
from . import ML_Model

def home(request):
    return render(request, 'index.html')

def result(request):
    # we need to get the values from the inputs
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])
    prediction = ML_Model.predict_Model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    return render(request, 'result.html', {'result': prediction})
