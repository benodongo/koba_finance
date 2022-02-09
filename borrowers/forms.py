from django import forms
from django.forms import ClearableFileInput, fields
from .models import Borrower, BorrowerContact, BorrowerKin, BorrowerCompany, BorrowerBank , BorrowersGroup , GroupMembers 

class NewBorrower(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['first_name','other_name','business_name', 'gender', 'title','mobile', 'email', 'dob','nationality',
        'marital_status','id_number','id_upload','kra_pin','pin_upload','number_of_children','number_of_dependants','credit_score',
        'borrower_photo', 'description', 'borrower_files']
        widgets = {
            'borrower_files': ClearableFileInput(attrs={'multiple':True}),
            'dob': forms.TextInput(attrs={'type': 'date'})
        }

class BorrowerForm1(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['first_name','other_name','business_name', 'reference', 'gender', 'title','mobile', 'email', 'dob','nationality',
        'marital_status','id_number','id_upload','kra_pin','pin_upload','number_of_children','number_of_dependants','credit_score',
        'borrower_photo', 'description', 'borrower_files']
        widgets = {
            'borrower_files': ClearableFileInput(attrs={'multiple': True}),
        }

class BorrowerForm2(forms.ModelForm):
    class Meta:
        model = BorrowerContact
        fields = ['email','phone_number','alt_phone','postal_address','postal_code','postal_city','county','sub_county','ward',
        'nearest_landmark','family_surname','name_of_chief','name_of_ass_chief','road_street','estate',
        'building_plot','house_office_no','Residence_Ownership',
        'landlord_name','caretaker_agent_name']

class BorrowerForm3(forms.ModelForm):
    class Meta:
        model = BorrowerKin
        fields = ['first_name','othernames','relationship','id_number','email','phone']

class BorrowerForm4(forms.ModelForm):
    class Meta:
        model = BorrowerCompany
        fields = ['company_name','year_of_registration','registration_number','lincense_number',
        'number_of_employees','business_lincense','certificate_of_incorporation','kra_pin','business_pin','nature_of_business']

class BorrowerForm5(forms.ModelForm):
    class Meta:
        model = BorrowerBank
        fields = ['account_name','bank','bank_branch','account_number','eft','mpesa_number']


class BorrowersGroupForm(forms.ModelForm):
    class Meta:
        model = BorrowersGroup
        fields = ['name', 'group_leader', 'collector_name', 'meeting_schedule', 'description']
        