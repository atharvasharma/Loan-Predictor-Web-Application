from django import forms


class DetailForm(forms.Form):
    RevolvingUtilizationOfUnsecuredLines = forms.FloatField(label='RevolvingUtilizationOfUnsecuredLines',widget=forms.TextInput(attrs={'placeholder': ' ( 0 to 1.5 )'}))
    Age=forms.IntegerField(label='Age',widget=forms.TextInput(attrs={'placeholder': ' ( 25 to 55 )'}))
    NumberOfTime30to59DaysPastDueNotWorse = forms.IntegerField(label='NumberOfTime30to59DaysPastDueNotWorse',widget=forms.TextInput(attrs={'placeholder': ' ( 0 to 5 )'}))
    DebtRatio= forms.FloatField(label='DebtRatio',widget=forms.TextInput(attrs={'placeholder': ' ( 0.02 to 10,000 )'}))
    MonthlyIncome=forms.IntegerField(label='MonthlyIncome',widget=forms.TextInput(attrs={'placeholder': ' ( 5000 to floating )'}))
    NumberOfOpenCreditLinesAndLoans=forms.IntegerField(label='NumberOfOpenCreditLinesAndLoans',widget=forms.TextInput(attrs={'placeholder': ' ( 0 to 6 )'}))
    NumberOfTimes90DaysLate=forms.IntegerField(label='NumberOfTimes90DaysLate',widget=forms.TextInput(attrs={'placeholder': ' ( 0 to 3 )'}))
    NumberRealEstateLoansOrLines=forms.IntegerField(label='NumberRealEstateLoansOrLines',widget=forms.TextInput(attrs={'placeholder': ' ( 0 to 5 )'}))
    NumberOfTime60to89DaysPastDueNotWorse=forms.IntegerField(label='NumberOfTime60to89DaysPastDueNotWorse',widget=forms.TextInput(attrs={'placeholder': ' ( 0 to 3 )'}))
    NumberOfDependents=forms.IntegerField(label='NumberOfDependents',widget=forms.TextInput(attrs={'placeholder': ' ( 0 to 4 )'}))
    Amount=forms.IntegerField(label='Amount',widget=forms.TextInput(attrs={'placeholder': '( Any amount )'}))
    Term=forms.IntegerField(label='Term',widget=forms.TextInput(attrs={'placeholder': '( 5 - 15 )'}))