from django.urls import path
from . import views

urlpatterns = [
    # Les differents urls du crud Customer
    path('list_customer',views.list_customer,name='list_customer'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('edit_customer/<int:id>',views.edit_customer,name='edit_customer'),
    path('info_customer/<int:id>',views.info_customer,name='info_customer'),
    path('delete_customer/<int:id>',views.delete_customer,name='delete_customer'),

    # Les differents urls du crud Sale
    path('list_sale',views.list_sale,name='list_sale'),
    path('add_sale',views.add_sale,name='add_sale'),
    #path('edit_sale/<int:id>',views.edit_sale,name='edit_sale'),
    path('info_sale/<int:id>',views.info_sale,name='info_sale'),
    path('delete_sale/<int:id>',views.delete_sale,name='delete_sale'),
]
