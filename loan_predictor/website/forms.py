from django import forms


class DetailForm(forms.Form):
    RevolvingUtilizationOfUnsecuredLines = forms.FloatField(label='RevolvingUtilizationOfUnsecuredLines')
    Age=forms.IntegerField(label='Age')
    NumberOfTime30to59DaysPastDueNotWorse = forms.IntegerField(label='NumberOfTime30to59DaysPastDueNotWorse')
    DebtRatio= forms.FloatField(label='DebtRatio')
    MonthlyIncome=forms.IntegerField(label='MonthlyIncome')
    NumberOfOpenCreditLinesAndLoans=forms.IntegerField(label='NumberOfOpenCreditLinesAndLoans')
    NumberOfTimes90DaysLate=forms.IntegerField(label='NumberOfTimes90DaysLate')
    NumberRealEstateLoansOrLines=forms.IntegerField(label='NumberRealEstateLoansOrLines')
    NumberOfTime60to89DaysPastDueNotWorse=forms.IntegerField(label='NumberOfTime60to89DaysPastDueNotWorse')
    NumberOfDependents=forms.IntegerField(label='NumberOfDependents')