from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import BorrowerForm2, BorrowerForm3, BorrowerForm4, BorrowerForm5, NewBorrower
from .models import Borrower, BorrowerBank, BorrowerCompany, BorrowerContact, BorrowerKin
from loans.models import Loan
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User

# Create your views here.
def newBorrower(request):
    if  request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        form = NewBorrower(request.POST, request.FILES)
        if form.is_valid():
            obj = Borrower()
            obj.first_name = form.cleaned_data['first_name']
            obj.other_name = form.cleaned_data['other_name']
            obj.business_name = form.cleaned_data['business_name']
            obj.reference = borrowerRef()
            obj.gender = form.cleaned_data['gender']
            obj.title = form.cleaned_data['title']
            obj.email = form.cleaned_data['email']
            obj.mobile = form.cleaned_data['mobile']
            obj.nationality = form.cleaned_data['nationality']
            obj.marital_status =form.cleaned_data['marital_status']
            obj.dob = form.cleaned_data['dob']
            obj.id_number = form.cleaned_data['id_number']
            obj.id_upload = request.FILES['id_upload']
            obj.kra_pin = form.cleaned_data['kra_pin']
            obj.pin_upload = request.FILES['pin_upload']
            obj.number_of_children = form.cleaned_data['number_of_children']
            obj.number_of_dependants = form.cleaned_data['number_of_dependants']
            obj.credit_score = form.cleaned_data['credit_score']
            obj.borrower_photo = request.FILES['borrower_photo']
            obj.description = form.cleaned_data['description']
            obj.borrower_files = request.FILES['borrower_files']
            #files = request.FIles.getlist('borrower_files')
            #for f in files:
            obj.modified_by = user
            obj.date_modified = datetime.now()
            obj.save()
            return redirect(borrowers)
        else:
            return HttpResponse("Form not valid")
    else:
        form = NewBorrower
        return render(request, 'borrowers/new_borrower.html', {'form':form})
        
def borrowers(request):
    context = {
        'borrowers': Borrower.objects.all()
    }
    return render(request, 'borrowers/borrowers.html', context)

def borrower_contact(request, b_id):
    context = {
        'contact': BorrowerContact.objects.get(borrower_id =b_id),
        'b_id':b_id
    }
    return render(request, 'borrowers/borrowers_contact.html',context)
def new_borrower_contact(request, b_id):
    if request.method == 'POST':
        form = BorrowerForm2(request.POST or None)
        if form.is_valid():
            borrower_id = int(request.session.get('borrower'))
            instance = Borrower.objects.get(id = borrower_id)
            obj = BorrowerContact()
            obj.borrower = instance
            obj.email = form.cleaned_data['email']
            obj.phone_number = form.cleaned_data['phone_number']
            obj.alt_phone = form.cleaned_data['alt_phone']
            obj.postal_address = form.cleaned_data['postal_address']
            obj.postal_code = form.cleaned_data['postal_code']
            obj.postal_city = form.cleaned_data['postal_city']
            obj.county = form.cleaned_data['county']
            obj.sub_county = form.cleaned_data['sub_county']
            obj.ward = form.cleaned_data['ward']
            obj.nearest_landmark = form.cleaned_data['nearest_landmark']
            obj.family_surname = form.cleaned_data['family_surname']
            obj.name_of_chief =form.cleaned_data['name_of_chief']
            obj.name_of_ass_chief = form.cleaned_data['name_of_ass_chief']
            obj.road_street = form.cleaned_data['road_street']
            obj.estate = form.cleaned_data['estate']
            obj.building_plot = form.cleaned_data['building_plot']
            obj.house_office_no = form.cleaned_data['house_office_no']
            obj.rental_choices = form.cleaned_data['rental_choices']
            obj.Residence_Ownership = form.cleaned_data['Residence_Ownership']
            obj.landlord_name = form.cleaned_data['landlord_name']
            obj.caretaker_agent_name = form.cleaned_data['caretaker_agent_name']
            obj.save()
            return redirect(borrower_contact, b_id=borrower_id)
    else:
        form = BorrowerForm2
        request.session['borrower'] = b_id
        return render(request, 'borrowers/new_borrower_contact.html',{'from':form})

def borrower_kin(request, b_id):
    context = {
        'kin': BorrowerKin.objects.get(borrower_id =b_id),
        'b_id':b_id
    }
    return render(request, 'borrowers/borrower_kin.html', context)
def new_borrower_kin(request, b_id):
    if request.method == 'POST':
        form = BorrowerForm3(request.POST or None)
        if form.is_valid():
            borrower_id = int(request.session.get('borrower'))
            instance = Borrower.objects.get(id = borrower_id)
            obj = BorrowerKin()
            obj.borrower = instance
            obj.first_name = form.cleaned_data['first_name']
            obj.othernames = form.cleaned_data['othernames']
            obj.relationship = form.cleaned_data['relationship']
            obj.id_number = form.cleaned_data['id_number']
            obj.email = form.cleaned_data['email']
            obj.phone = form.cleaned_data['phone']
            obj.save()
            return redirect(borrower_kin, b_id =borrower_id)
    else:
        form = BorrowerForm3
        request.session['borrower'] = b_id
        return render(request, 'borrowers/new_borrower_kin.html',{'from':form})

def borrower_company(request, b_id):
    context = {
        'company': BorrowerCompany.objects.get(borrower_id =b_id),
        'b_id':b_id
    }
    return render(request , 'borrowers/borrower_company.html', context)

def new_borrower_company(request, b_id):
    if request.method == 'POST':
        form = BorrowerForm4(request.POST, request.FILES)
        if form.is_valid():
            borrower_id = int(request.session.get('borrower'))
            instance = Borrower.objects.get(id = borrower_id)
            obj = BorrowerCompany()
            obj.borrower = instance
            obj.company_name = form.cleaned_data['company_name']
            obj.year_of_registration = form.cleaned_data['year_of_registration']
            obj.registration_number = form.cleaned_data['registration_number']
            obj.lincense_number = form.cleaned_data['lincense_number']
            obj.number_of_employees = form.cleaned_data['number_of_employees']
            obj.business_lincense = request.Files['business_lincense']
            obj.certificate_of_incorporation = request.Files['certificate_of_incorporation']
            obj.kra_pin = form.cleaned_data['kra_pin']
            obj.business_pin = request.Files['business_pin']
            obj.nature_of_business = form.cleaned_data['nature_of_business']
            obj.save()
            return redirect(borrower_company, b_id =borrower_id)
    else:
        form = BorrowerForm4
        request.session['borrower'] = b_id
        return render(request, 'borrowers/new_borrower_company.html',{'from':form})

def borrower_bank(request, b_id):
    context = {
        'bank':BorrowerBank.objects().get(borrower_id = b_id),
        'b_id':b_id
    }
    return render(request, 'borrowers/borrower_bank.html', context)

def new_borrower_bank(request, b_id):
    if request.method == 'POST':
        form = BorrowerForm5(request.POST or None )
        if form.is_valid():
            borrower_id = int(request.session.get('borrower'))
            instance = Borrower.objects.get(id = borrower_id)
            obj = BorrowerBank()
            obj.borrower = instance
            obj.account_name  = form.cleaned_data['account_name']
            obj.bank = form.cleaned_data['bank']
            obj.bank_branch = form.cleaned_data['bank_branch']
            obj.account_number = form.cleaned_data['account_number']
            obj.eft = form.cleaned_data['eft']
            obj.mpesa_number = form.cleaned_data['mpesa_number']
            obj.save()
            return redirect(borrower_bank, b_id=borrower_id)
        else:
            return HttpResponse('form invalid')

    else:
        form = BorrowerForm5
        request.session['borrower'] = b_id
        return render(request, 'borrowers/new_borrower_bank.html', {'form':form})

def borrower_profile(request, b_id):
    context ={
        'borrower': Borrower.objects.get(id = b_id),
        'contact' : BorrowerContact.objects.filter(borrower_id = b_id),
        'kin': BorrowerKin.objects.filter(borrower_id = b_id),
        'company':BorrowerCompany.objects.filter(borrower_id = b_id),
        'bank':BorrowerBank.objects.filter(borrower_id = b_id),
        'loans':Loan.objects.all().filter(borrower_id = b_id),
    }
    return render(request, 'borrowers/borrower_profile.html', context)

##############################
class BorrowerWizard(SessionWizardView):
    template_name = "borrowers/new_borrower.html"
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'borrower_files'))
    def done(self, form_list, **kwargs):
        do_something_with_the_form_data(form_list)
       
        return render(self.request, 'borrowers/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

#generate loan reference
def borrowerRef():
    serial = ""
    borrower = Borrower.objects.all().order_by('-reference').first() 
    if borrower:
        if borrower.reference == None:
            serial = '000001'
        else:
            next = int(borrower.reference) +1
            serial = serial = str(next).rjust(6,'0')
       
    else:
        serial = '000001'
        
    return serial


#Africastalking
@csrf_exempt
@require_http_methods(["POST"])
def incoming_messages(request):
    date = request.POST.get('date')
    text = request.POST.get('text')
    phoneNo = request.POST.get('from')
    to = request.POST.get('to')
    linkId = request.POST.get('linkId')
  
    print(text)
    print(phoneNo)
    print(date)
    print(to)
    print(linkId)
    #TODO SAVE TO DB

    return HttpResponse(status=200)
