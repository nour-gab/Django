from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField 
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from store.models import Product, OrderItem, Customer, Collection
from tags.models import TggedItem

# Create your views here.



def say_hello(request):

    #queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(price__lt=20))
    # queryset= Product.objects.raw('SELECT * FROM store_product')
    # with connection.cursor() as cursor:
    #     cursor.execute()
    #     cursor.callproc('get_cusotmer', [1,2,'a'])

    # #queryset = Product.objects.filter(collection__id=3).order_by('price')[:5].values_list('id' ,'title' ,'collection__title')
    #select_related --1 instance || prefetch_related
    #queryset=Product.objects.prefetch_related('promotions').all()
    #result = Product.objects.aggregate(count= Count('id') ,min_price= Min('price'))
    # queryset = Customer.objects.annotate(
    #     full_name = Func(F('first_name'), Value(' '), F('last_name'), function= 'CONCAT')
    # )

    # queryset = Customer.objects.annotate(
    #     full_name = Concat('first_name', Value(' '), 'last_name'),
    #     orders_count= Count('order') 
    # )

    # discounted= ExpressionWrapper(F('price') * 0.8, output_field= DecimalField())
    # queryset= Product.objects.annotate(
    #     discounted_price= discounted 
    # )

    #queryset= TggedItem.objects.get_tags_for(Product, 1)

    # collection= Collection()
    # collection.title= 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()

    #Collection.objects.filter(pk=1001).update(featured_product= None)
    #Collection.objects.filter(id__gt=10).delete()


    return render(request, 'hello.html', {'name': 'Nour'})