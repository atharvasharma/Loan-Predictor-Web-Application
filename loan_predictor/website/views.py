#ml
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import _pickle
from mortgage import Loan
#django
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import DetailForm


# Create your views here.
def index (request):
	template = loader.get_template('website/index.html')
	return HttpResponse(template.render({}, request))


def details(request):
    load_model1=open("models/model1.pkl","rb")
    lin_reg_model1=joblib.load(load_model1)

    load_model2=open("models/model2.pkl","rb")
    lin_reg_model2=joblib.load(load_model2)

    load_model3=open("models/model3.pkl","rb")
    lin_reg_model3=joblib.load(load_model3)

    load_model4=open("models/model4.pkl","rb")
    lin_reg_model4=joblib.load(load_model4)

    load_model5=open("models/model5.pkl","rb")
    lin_reg_model5=joblib.load(load_model5)

    load_model6=open("models/model6.pkl","rb")
    lin_reg_model6=joblib.load(load_model6)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DetailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            RevolvingUtilizationOfUnsecuredLines=form.cleaned_data['RevolvingUtilizationOfUnsecuredLines']
            Age=form.cleaned_data['Age']
            NumberOfTime30to59DaysPastDueNotWorse=form.cleaned_data['NumberOfTime30to59DaysPastDueNotWorse']
            DebtRatio=form.cleaned_data['DebtRatio']
            MonthlyIncome=form.cleaned_data['MonthlyIncome']
            NumberOfOpenCreditLinesAndLoans=form.cleaned_data['NumberOfOpenCreditLinesAndLoans']
            NumberOfTimes90DaysLate=form.cleaned_data['NumberOfTimes90DaysLate']
            NumberRealEstateLoansOrLines=form.cleaned_data['NumberRealEstateLoansOrLines']
            NumberOfTime60to89DaysPastDueNotWorse=form.cleaned_data['NumberOfTime60to89DaysPastDueNotWorse']
            NumberOfDependents=form.cleaned_data['NumberOfDependents']
            Amount=form.cleaned_data['Amount']
            Term=form.cleaned_data['Term']
            datas=[]
            datas.extend((
                RevolvingUtilizationOfUnsecuredLines,
                Age,
                NumberOfTime30to59DaysPastDueNotWorse,
                DebtRatio,
                MonthlyIncome,
                NumberOfOpenCreditLinesAndLoans,
                NumberOfTimes90DaysLate,
                NumberRealEstateLoansOrLines,
                NumberOfTime60to89DaysPastDueNotWorse,
                NumberOfDependents
            ))
            datas=[float(i) for i in datas]
            datas=[datas]
            print(datas)
            mypred1=lin_reg_model1.predict(datas)
            mypred1=np.round(mypred1)
            print(mypred1)

            mypred2=lin_reg_model2.predict(datas)
            mypred2=np.round(mypred2)
            print(mypred2)

            mypred3=lin_reg_model3.predict(datas)
            mypred3=np.round(mypred3)
            print(mypred3)

            mypred4=lin_reg_model4.predict(datas)
            mypred4=np.round(mypred4)
            print(mypred4)

            mypred5=lin_reg_model5.predict(datas)
            mypred5=np.round(mypred5)
            print(mypred5)

            mypred6=lin_reg_model6.predict(datas)
            mypred6=np.round(mypred6)
            print(mypred6)
            #print(RevolvingUtilizationOfUnsecuredLines)
            #print(Age)
            #print(NumberOfTime30to59DaysPastDueNotWorse)
            #print(DebtRatio)
            #print(MonthlyIncome)load:
            #print(NumberOfOpenCreditLinesAndLoans)
            #print(NumberOfTimes90DaysLate)
            #print(NumberRealEstateLoansOrLines)
            #print(NumberOfTime60to89DaysPastDueNotWorse)
            #print(NumberOfDependents)
            #print(Amount)
            #print(Term)
            TotalAmount1=Amount+Amount*Term*0.06            
            Monthly1=(TotalAmount1/Term)/12

            TotalAmount2=Amount+Amount*Term*0.07           
            Monthly2=(TotalAmount1/Term)/12

            TotalAmount3=Amount+Amount*Term*0.065           
            Monthly3=(TotalAmount1/Term)/12

            TotalAmount4=Amount+Amount*Term*0.075            
            Monthly4=(TotalAmount1/Term)/12

            TotalAmount5=Amount+Amount*Term*0.08           
            Monthly5=(TotalAmount1/Term)/12

            TotalAmount6=Amount+Amount*Term*0.05            
            Monthly6=(TotalAmount1/Term)/12
            context={
                'mypred1':mypred1,
                'mypred2':mypred2,
                'mypred3':mypred3,
                'mypred4':mypred4,
                'mypred5':mypred5,
                'mypred6':mypred6,
                'RevolvingUtilizationOfUnsecuredLines':RevolvingUtilizationOfUnsecuredLines,
                'Age':Age,
                'NumberOfTime30to59DaysPastDueNotWorse':NumberOfTime30to59DaysPastDueNotWorse,
                'DebtRatio':DebtRatio,
                'MonthlyIncome':MonthlyIncome,
                'NumberOfOpenCreditLinesAndLoans':NumberOfOpenCreditLinesAndLoans,
                'NumberOfTimes90DaysLate':NumberOfTimes90DaysLate,
                'NumberRealEstateLoansOrLines':NumberRealEstateLoansOrLines,
                'NumberOfTime60to89DaysPastDueNotWorse':NumberOfTime60to89DaysPastDueNotWorse,
                'NumberOfDependents':NumberOfDependents,
                'Amount':Amount,
                'Term':Term,
                'TotalAmount1':TotalAmount1,
                'Monthly1':Monthly1,
                'TotalAmount2':TotalAmount2,
                'Monthly2':Monthly2,
                'TotalAmount3':TotalAmount3,
                'Monthly3':Monthly3,
                'TotalAmount4':TotalAmount4,
                'Monthly4':Monthly4,
                'TotalAmount5':TotalAmount5,
                'Monthly5':Monthly5,
                'TotalAmount6':TotalAmount6,
                'Monthly6':Monthly6,
            }
            
            return render(request,'website/results.html',context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = DetailForm()

    return render(request, 'website/details.html', {'form': form})
	
