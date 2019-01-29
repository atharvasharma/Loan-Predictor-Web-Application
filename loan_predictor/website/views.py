from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import DetailForm
# Create your views here.
def index (request):
	template = loader.get_template('website/index.html')
	return HttpResponse(template.render({}, request))


def details(request):
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
            print(RevolvingUtilizationOfUnsecuredLines)
            print(Age)
            print(NumberOfTime30to59DaysPastDueNotWorse)
            print(DebtRatio)
            print(MonthlyIncome)
            print(NumberOfOpenCreditLinesAndLoans)
            print(NumberOfTimes90DaysLate)
            print(NumberRealEstateLoansOrLines)
            print(NumberOfTime60to89DaysPastDueNotWorse)
            print(NumberOfDependents)
            return HttpResponse('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DetailForm()

    return render(request, 'website/details.html', {'form': form})
	
