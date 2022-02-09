from  django.urls import path
from . import views

urlpatterns = [
    path('loans',views.loans, name='loans'),
    path('new_loan/<int:b_id>/', views.new_loan , name='new_loan'),
    path('my_loans/<int:b_id>/', views.my_loans , name='my_loans'),
    path('approve_loan/<int:loan_id>/', views.approve_loan, name='approve_loan'),
    
]