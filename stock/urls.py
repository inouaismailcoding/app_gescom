from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('download_file_type/?format=excel',views.download_file_type,name='download_file_type'),
    path('download_file_type/?format=csv',views.download_file_type,name='download_file_type'),
    path('download_file_type/?format=json',views.download_file_type,name='download_file_type'),

    # Path Crud Category
    path("list_category/", views.list_category, name="list_category"),
    path('stock/add_category',views.add_category,name="add_category"),
    path('stock/edit_category/<int:id>',views.edit_category,name="edit_category"),
    path('stock/delete_category/<int:id>',views.delete_category,name="delete_category"),
    path('stock/info_category/<int:id>',views.info_category,name="info_category"),
    
    # path Crud Package
    path("list_package/", views.list_package, name="list_package"),
    path('stock/add_package',views.add_package,name="add_package"),
    path('stock/edit_package/<int:id>',views.edit_package,name="edit_package"),
    path('stock/delete_package/<int:id>',views.delete_package,name="delete_package"),
    path('stock/info_package/<int:id>',views.info_package,name="info_package"),
    
    # Path Crud Article
    path("list_article/", views.list_article, name="list_article"),
    path('stock/add_article',views.add_article,name="add_article"),
    path('stock/edit_article/<int:id>',views.edit_article,name="edit_article"),
    path('stock/delete_article/<int:id>',views.delete_article,name="delete_article"),
    path('stock/info_article/<int:id>',views.info_article,name="info_article"),
    
    # 
    

]
