from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Max, Min, Avg
from store.models import Product, OrderItem, Customer

# Create your views here.



def say_hello(request):

    #queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(price__lt=20))
    #queryset = Product.objects.filter(collection__id=3).order_by('price')[:5].values_list('id' ,'title' ,'collection__title')
    #select_related --1 instance || prefetch_related
    #queryset=Product.objects.prefetch_related('promotions').all()
    #result = Product.objects.aggregate(count= Count('id') ,min_price= Min('price'))
    queryset = Customer.objects.annotate(is_new=Value(True))

    return render(request, 'hello.html', {'name': 'Nour', 'result': list(queryset)})