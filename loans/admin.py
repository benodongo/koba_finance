from django.contrib import admin
from .models import LoanProduct , Loan , RepaymentCycle, GuarantorRelationShip , Guarantor

# Register your models here.
admin.site.register(LoanProduct)
admin.site.register(RepaymentCycle)
admin.site.register(Loan)
admin.site.register(GuarantorRelationShip)
admin.site.register(Guarantor)