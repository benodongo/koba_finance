from django import forms
from django.forms import fields, widgets
from .models import Loan, LoanApproval, LoanRepayment

class LoanForm(forms.ModelForm):
    class Meta:
        model= Loan
        fields=['loan_product', 'means_disbursed','principal_amount','loan_release_date',
        'interest_method','interest_type','loan_interest', 'rate_cycle','loan_duration',
        'repayment_cycle','number_of_repayments','loan_application_fee']
        widgets = {
            'loan_release_date': forms.TextInput(attrs={'type': 'date'})
        }

class LoanApprovalForm(forms.ModelForm):
    class Meta:
        model= LoanApproval
        fields=['documents_confirmation','remarks', 'credit_score_check','status']
class LoanRepaymentForm(forms.ModelForm):
    class Meta:
        model = LoanRepayment
        fields = ['payment_method', 'amount', 'date_collected']