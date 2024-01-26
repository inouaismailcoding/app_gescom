from django.urls import path
from . import views


urlpatterns = [
    path("list_intervenant",views.list_intervenant,name="list_intervenant"),
    path("add_intervenant",views.add_intervenant,name="add_intervenant"),
    path("edit_intervenant/<int:id>",views.edit_intervenant,name="edit_intervenant"),
    path("delete_intervenant/<int:id>",views.delete_intervenant,name="delete_intervenant"),
    path("info_intervenant/<int:id>",views.info_intervenant,name="info_intervenant"),


    path("list_transaction",views.list_transaction,name="list_transaction"),
    path("add_transaction",views.add_transaction,name="add_transaction"),
    path("delete_transaction/<int:id>",views.delete_transaction,name="delete_transaction"),
    path("info_transaction/<int:id>",views.info_transaction,name="info_transaction"),
    path("report_transaction",views.report_transaction,name="report_transaction"),


]
