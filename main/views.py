from django.shortcuts import render
from store.models import Customer

# Create your views here.
def home(request):
    query_set = Customer.objects.all()
    for customer in query_set:
        print((customer))
    return render(request, 'index.html',{'name':'Sanzid Olioul'})