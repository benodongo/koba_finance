from datetime import datetime
from borrowers.models import Borrower
from django.forms.models import ModelForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from .models import Loan, LoanApproval, LoanRepayment
from .forms import LoanForm , LoanApprovalForm, LoanRepaymentForm
from django.contrib.auth.models import User

# Create your views here.
def new_loan(request,b_id):
    if request.method == 'POST':
        form = LoanForm(request.POST or None)
        if form.is_valid():
            borrower_id = int(request.session.get('borrower'))
            instance = Borrower.objects.get(id = borrower_id)
            obj = Loan()
            obj.borrower = instance
            obj.loan_product = form.cleaned_data['loan_product']
            obj.loan_ref = loanRef()
            obj.means_disbursed = form.cleaned_data['means_disbursed']
            obj.principal_amount = form.cleaned_data['principal_amount']
            obj.loan_release_date = form.cleaned_data['loan_release_date']
            obj.interest_method = form.cleaned_data['interest_method']
            obj.interest_type = form.cleaned_data['interest_type']
            obj.loan_interest = form.cleaned_data['loan_interest']
            obj.rate_cycle = form.cleaned_data['rate_cycle']
            obj.loan_duration = form.cleaned_data['loan_duration']
            obj.repayment_cycle = form.cleaned_data['repayment_cycle']
            obj.number_of_repayments = form.cleaned_data['number_of_repayments']
            obj.loan_application_fee = form.cleaned_data['loan_application_fee']
            obj.loan_status = '1'
            obj.save()
            return redirect(my_loans, b_id=borrower_id)
        else:
            HttpResponse("Form not valid")

    else:
        form = LoanForm
        request.session['borrower'] =b_id
        return render(request, 'loans/new_loan.html', {'form':form})



def loans(request):
    context = {
        'loans':Loan.objects.all()
    }
    return render(request, 'loans/loans.html', context)

def my_loans(request, b_id):
    context = {
        'loans':Loan.objects.all().filter(borrower_id = b_id),
        'b_id':b_id
    }
    return render(request, 'loans/loan.html', context)

def approve_loan(request, loan_id):
    if request.method == 'POST':
        loan = Loan.objects.get(id = loan_id)
        user = User.objects.get(id=request.user.id)
        form = LoanApprovalForm(request.POST or None)
        if form.is_valid():
            obj = LoanApproval()
            obj.loan = loan
            obj.remarks = form.cleaned_data['remarks']
            obj.documents_confirmation = form.cleaned_data['documents_confirmation']
            obj.credit_score_check = form.cleaned_data['documents_confirmation']
            obj.status = form.cleaned_data['status']
            obj.approved_by = user
            obj.date_approved = datetime.now()
            obj.save()
            #TODO Update loan status in loans table-
            if obj.status == '1':
                loan.loan_status = '3'
                loan.save()
            return redirect(my_loans, b_id=loan.borrower_id)

    else:
        form = LoanApprovalForm
        loan = Loan.objects.get(id = loan_id)
        context = {
            'loan':Loan.objects.get(id = loan_id),
            'form':form,
            'loans':Loan.objects.all().filter(borrower_id = loan.borrower_id).order_by('-loan_ref'),
            'borrower':Borrower.objects.get(id = loan.borrower_id)

        }
        request.session['loan'] =loan_id
        return render(request, 'loans/approve_loan.html', context)

def repayment(request, loan_id):
    if request.method == 'POST':
        loan = Loan.objects.get(id = loan_id)
        user = User.objects.get(id=request.user.id)
        form = LoanRepaymentForm(request.POST or None)
        if form.is_valid():
            obj = LoanRepayment()
            obj.loan = loan
            obj.payment_method = form.cleaned_data['payment_method']
            obj.amount = form.cleaned_data['amount']
            obj.date_collected = form.cleaned_data['date_collected']
            obj.collected_by = user
            obj.date_modified = datetime.now
            obj.save
            return redirect(my_loans, b_id=loan.borrower_id)
    else:
    
        form = LoanRepaymentForm
        loan = Loan.objects.get(id = loan_id)
        context = {
        'loan':Loan.objects.get(id = loan_id),
        'form':form,
        'loans':Loan.objects.all().filter(borrower_id = loan.borrower_id).order_by('-loan_ref'),
        'borrower':Borrower.objects.get(id = loan.borrower_id)
        }

    
        request.session['loan'] =loan_id
        return render(request, 'loans/repay_loan.html', context)

        
#generate loan reference
def loanRef():
    serial = ""
    loan = Loan.objects.all().order_by('-loan_ref').first() 
    if loan:
        if loan.loan_ref == None:
            serial = '000001'
        else:
            next = int(loan.loan_ref) +1
            serial = serial = str(next).rjust(6,'0')
       
    else:
        serial = '000001'
        
    return serial

