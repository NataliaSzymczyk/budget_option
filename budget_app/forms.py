from django import forms
from .models import Budget, PiggyBanks, MonthsBudget, Stock, AlreadyCollected, PaymentDay, Credits, Repayment, RepaymentDay, Income, AdditionalIncome
from .views import *


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(BudgetForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class PiggyBanksForm(forms.ModelForm):
    class Meta:
        model = PiggyBanks
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(PiggyBanksForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class MonthsBudgetForm(forms.ModelForm):
    class Meta:
        model = MonthsBudget
        exclude = ['month_date']
    def __init__(self, *args, **kwargs):
        super(MonthsBudgetForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        self.fields['value_of'].required = False
        self.fields['dividend'].required = False
        self.fields['type_of_market'].required = False
        self.fields['www'].required = False


class CreditsForm(forms.ModelForm):
    class Meta:
        model = Credits
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CreditsForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['should_end_on'].required = False


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['income_description'].required = False


class AdditionalIncomeForm(forms.ModelForm):
    class Meta:
        model = AdditionalIncome
        exclude = ['income_date']
    def __init__(self, *args, **kwargs):
        super(AdditionalIncomeForm, self).__init__(*args, **kwargs)
        self.fields['amount_only'].required = False
        self.fields['amount_with_monthly'].required = False
        self.fields['income_description'].required = False
