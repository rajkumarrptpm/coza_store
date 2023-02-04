from django.urls import path
from frontend import views

urlpatterns=[
    path("",views.homefctn,name="homefctn"),
    path("userloginfctn/",views.userloginfctn,name="userloginfctn"),
    path("contact_fctn/",views.contact_fctn,name="contact_fctn"),
    path("product_fctn/",views.product_fctn,name="product_fctn"),
    path("prdt_dtls_fctn/<int:dataid>",views.prdt_dtls_fctn,name="prdt_dtls_fctn"),
    path("about_fctn/",views.about_fctn,name="about_fctn"),
    path("cart_fctn/",views.cart_fctn,name="cart_fctn"),
    path("logout_fctn1/",views.logout_fctn1,name="logout_fctn1"),
    path("reg_data/",views.reg_data,name="reg_data"),
    path("login_dtls_fctn/",views.login_dtls_fctn,name="login_dtls_fctn"),
    path("save_contact_us_fctn/",views.save_contact_us_fctn,name="save_contact_us_fctn"),
    path("disctgryfctn/<itemctgry>/",views.disctgryfctn,name="disctgryfctn"),
    path("dis_brand_fctn/<itembrnd>",views.dis_brand_fctn,name="dis_brand_fctn"),
]