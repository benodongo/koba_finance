from django.contrib import admin

from .models import Borrower, Bank, BankBranch, BorrowerBank, BorrowerCompany,BorrowerContact, BorrowerKin, County,SubCounty,Ward
admin.site.register(Borrower )
admin.site.register(Bank)
admin.site.register(BankBranch)
admin.site.register(BorrowerBank)
admin.site.register(BorrowerCompany)
admin.site.register(BorrowerContact)
admin.site.register(BorrowerKin)
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Ward)
