from  django.urls import path
from . import views
from .forms import BorrowerForm1, BorrowerForm2, BorrowerForm3, BorrowerForm4, BorrowerForm5

urlpatterns =[
    path('new/', views.newBorrower, name='borrower'),
    path('all',views.borrowers, name='borrowers'),
    path('borrower_profile/<int:b_id>/', views.borrower_profile , name='borrower_profile'),
     path('sms',views.incoming_messages, name='sms'),
]