from django.urls import path
from . import views 

urlpatterns = [
    path('list_supplier',views.list_supplier,name="list_supplier"),
    path('add_supplier',views.add_supplier,name="add_supplier"),
    path('edit_supplier/<int:id>',views.edit_supplier,name="edit_supplier"),
    path('delete_supplier/<int:id>',views.delete_supplier,name="delete_supplier"),
    path('info_supplier/<int:id>',views.info_supplier,name="info_supplier"),

    path('list_purchase',views.list_purchase,name="list_purchase"),
    path('add_purchase',views.add_purchase,name="add_purchase"),
    path('delete_purchase/<int:id>',views.delete_purchase,name="delete_purchase"),
    path('info_purchase/<int:id>',views.info_purchase,name="info_purchase"),

]
