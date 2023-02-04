from django.urls import path
from backend import views

urlpatterns=[
    path("indexfctn/",views.indexfctn,name="indexfctn"),
    path("loginfctn/",views.loginfctn,name="loginfctn"),
    path("addloginfctn/",views.addloginfctn,name="addloginfctn"),
    path("logout_fctn/",views.logout_fctn,name="logout_fctn"),
    path("Messagefctn/",views.Messagefctn,name="Messagefctn"),



    path("add_category_fctn/",views.add_category_fctn,name="add_category_fctn"),
    path("save_category_fctn/",views.save_category_fctn,name="save_category_fctn"),
    path("display_category_fctn/",views.display_category_fctn,name="display_category_fctn"),
    path('edit_category_fctn/<int:dataid>/', views.edit_category_fctn, name="edit_category_fctn"),
    path("Update_category_fctn/<int:dataid>/", views.Update_category_fctn, name="Update_category_fctn"),
    path("delete_category_fctn/<int:dataid>/", views.delete_category_fctn, name="delete_category_fctn"),




    path("add_product_fctn/", views.add_product_fctn, name="add_product_fctn"),
    path("display_product_fctn/",views.display_product_fctn,name="display_product_fctn"),
    path("save_add_product_fctn/",views.save_add_product_fctn,name="save_add_product_fctn"),
    path('edit_product_fctn/<int:dataid>/', views.edit_product_fctn, name="edit_product_fctn"),
    path("Update_product_fctn/<int:dataid>/", views.Update_product_fctn, name="Update_product_fctn"),
    path("delete_prdt_fctn/<int:dataid>/", views.delete_prdt_fctn, name="delete_prdt_fctn"),




    path("add_brand_fctn/", views.add_brand_fctn, name="add_brand_fctn"),
    path("display_brand_fctn/",views.display_brand_fctn,name="display_brand_fctn"),
    path("save_brand_fctn/",views.save_brand_fctn,name="save_brand_fctn"),
    path('edit_brand_fctn/<int:dataid>/', views.edit_brand_fctn, name="edit_brand_fctn"),
    path("Update_brand_fctn/<int:dataid>/", views.Update_brand_fctn, name="Update_brand_fctn"),
    path("delete_brand_fctn/<int:dataid>/", views.delete_brand_fctn, name="delete_brand_fctn"),




    path("add_size_fctn/", views.add_size_fctn, name="add_size_fctn"),
    path("display_size_fctn/", views.display_size_fctn, name="display_size_fctn"),
    path("save_size_fctn/", views.save_size_fctn, name="save_size_fctn"),
    path('edit_size_fctn/<int:dataid>/', views.edit_size_fctn, name="edit_size_fctn"),
    path("Update_size_fctn/<int:dataid>/", views.Update_size_fctn, name="Update_size_fctn"),
    path("delete_size_fctn/<int:dataid>/", views.delete_size_fctn, name="delete_size_fctn"),

]