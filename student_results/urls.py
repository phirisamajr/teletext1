from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views 
from django.urls import reverse





urlpatterns = [    
    path('', views.home, name = "home"),
    url(r'^secondary/$', views.secondary_page, name="secondary_page"),
    url(r'^techschool/$', views.techschool_page, name="techschool_page"),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.change_friends, name="change_friends"),
    url(r'^primary/$', views.plevel_page, name="plevel_page"),
    url(r'^friends/$', views.FriendPage, name="FriendPage"),
    url(r'^searchfriends/$', views.SearchFriend, name="SearchFriend"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^about/$', views.aboutPage, name="aboutPage"),
    url(r'^donate/$', views.donationPage, name="donationPage"),
    url(r'^profile/edit_profile/$', views.edit_profile, name="edit_profile"),
    url(r'^apload_excel/$', views.apload_excel, name="apload_excel"),

    
    url(r'^posts/$', views.PostPage, name="PostPage"),
    url(r'^post_detail/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.PostPageDetail, name = "PostPageDetail"),
    url(r'^updatepost/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updatePost, name = "updatePost"),
    url(r'^deletepost/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deletePost, name = "deletePost"),
    url(r'^posts/addpost/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.addpostpage, name = "addpostpage"),
    

    url(r'^secondary/formfive_egm/$', views.egm5_list, name="egm5_list"),
    url(r'^secondary/formfive_egm/addfive_egm/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.EGM5Page, name = "EGM5Page"),
    url(r'^updatefiveegm/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateEGM5, name = "updateEGM5"),
    url(r'^deletefiveegm/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteEGM5, name = "deleteEGM5"),


    url(r'^techschool/formfourtech/$', views.formfourtech_list, name="formfourtech_list"),
    url(r'^techschool/formfourtech/addf4t/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.FormfourTechPage, name = "FormfourTechPage"),
    url(r'^updatef4tech/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateFormFourTech, name = "updateFormFourTech"),
    url(r'^deletef4tech/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteFormFourTech, name = "deleteFormFourTech"),


    url(r'^techschool/formthreetech/$', views.formthreetech_list, name="formthreetech_list"),
    url(r'^techschool/formthreetech/addf1t/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.FormthreeTechPage, name = "FormthreeTechPage"),
    url(r'^updatef3tech/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateFormThreeTech, name = "updateFormThreeTech"),
    url(r'^deletef3tech/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteFormThreeTech, name = "deleteFormThreeTech"),


    url(r'^techschool/formtwotech/$', views.formtwotech_list, name="formtwotech_list"),
    url(r'^techschool/formtwotech/addf1t/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.FormtwoTechPage, name = "FormtwoTechPage"),
    url(r'^updatef2tech/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateFormTwoTech, name = "updateFormTwoTech"),
    url(r'^deletef2tech/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteFormTwoTech, name = "deleteFormTwoTech"),


    url(r'^techschool/formonetech/$', views.formonetech_list, name="formonetech_list"),
    url(r'^techschool/formonetech/addf1t/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.FormoneTechPage, name = "FormoneTechPage"),
    url(r'^updatef1tech/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateFormOneTech, name = "updateFormOneTech"),
    url(r'^deletef1tech/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteFormOneTech, name = "deleteFormOneTech"),


    url(r'^secondary/formfour/$', views.formfour_list, name="formfour_list"),
    url(r'^secondary/formfour/addf4/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.FormfourPage, name = "FormfourPage"),
    url(r'^updatef4/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateFormFour, name = "updateFormFour"),
    url(r'^deletef4/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteFormFour, name = "deleteFormFour"),


    url(r'^secondary/formthree/$', views.formthree_list, name="formthree_list"),
    url(r'^secondary/formthree/addf3/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.FormthreePage, name = "FormthreePage"),
    url(r'^updatef3/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateFormThree, name = "updateFormThree"),
    url(r'^deletef3/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteFormThree, name = "deleteFormThree"),

    url(r'^secondary/formtwo/$', views.formtwo_list, name="formtwo_list"),
    url(r'^secondary/formtwo/addf2/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.FormtwoPage, name = "FormtwoPage"),
    url(r'^updatef2/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateFormTwo, name = "updateFormTwo"),
    url(r'^deletef2/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteFormTwo, name = "deleteFormTwo"),

    url(r'^secondary/formone/$', views.formone_list, name="formone_list"),
    url(r'^secondary/formone/addf1/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.FormonePage, name = "FormonePage"),
    url(r'^updatef1/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateFormOne, name = "updateFormOne"),
    url(r'^deletef1/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteFormOne, name = "deleteFormOne"),



    url(r'^primary/standardone/$', views.std1_list, name="std1_list"),
    url(r'^add1/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.std1Page, name = "std1Page"),
    url(r'^update1/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateStd1, name = "updateStd1"),
    url(r'^delete1/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteStd1, name = "deleteStd1"),

    url(r'^primary/standardtwo/$', views.std2_list, name="std2_list"),
    url(r'^add2/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.std2Page, name = "std2Page"),
    url(r'^update2/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateStd2, name = "updateStd2"),
    url(r'^delete2/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteStd2, name = "deleteStd2"),

    url(r'^primary/standardthree/$', views.std3_list, name="std3_list"),
    url(r'^add3/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.std3Page, name = "std3Page"),
    url(r'^update3/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateStd3, name = "updateStd3"),
    url(r'^delete3/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteStd3, name = "deleteStd3"),

    url(r'^primary/standardfour/$', views.std4_list, name="std4_list"),
    url(r'^add4/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.std4Page, name = "std4Page"),
    url(r'^update4/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateStd4, name = "updateStd4"),
    url(r'^delete4/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteStd4, name = "deleteStd4"),

    url(r'^primary/standardfive/$', views.std5_list, name="std5_list"),
    url(r'^add5/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.std5Page, name = "std5Page"),
    url(r'^update5/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateStd5, name = "updateStd5"),
    url(r'^delete5/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteStd5, name = "deleteStd5"),

    url(r'^primary/standardsix/$', views.std6_list, name="std6_list"),
    url(r'^add6/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.std6Page, name = "std6Page"),
    url(r'^update6/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateStd6, name = "updateStd6"),
    url(r'^delete6/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteStd6, name = "deleteStd6"),

    url(r'^primary/standardseven/$', views.std7_list, name="std7_list"),
    url(r'^add7/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.std7Page, name = "std7Page"),
    url(r'^update7/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.updateStd7, name = "updateStd7"),
    url(r'^delete7/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.deleteStd7, name = "deleteStd7"),
    
    url(r'^saris/$', views.saris_page, name="saris_page"),
    url(r'^saris_frm4t/$', views.sarisfrm4t, name="sarisfrm4t"),
    url(r'^saris_frm3t/$', views.sarisfrm3t, name="sarisfrm3t"),
    url(r'^saris_frm2t/$', views.sarisfrm2t, name="sarisfrm2t"),
    url(r'^saris_frm1t/$', views.sarisfrm1t, name="sarisfrm1t"),
    url(r'^saris_frm4/$', views.sarisfrm4, name="sarisfrm4"),
    url(r'^saris_frm3/$', views.sarisfrm3, name="sarisfrm3"),
    url(r'^saris_frm2/$', views.sarisfrm2, name="sarisfrm2"),
    url(r'^saris_frm1/$', views.sarisfrm1, name="sarisfrm1"),
    url(r'^saris_std1/$', views.sarisstd1, name="sarisstd1"),
    url(r'^saris_std2/$', views.sarisstd2, name="sarisstd2"),
    url(r'^saris_std3/$', views.sarisstd3, name="sarisstd3"),
    url(r'^saris_std4/$', views.sarisstd4, name="sarisstd4"), 
    url(r'^saris_std5/$', views.sarisstd5, name="sarisstd5"),
    url(r'^saris_std6/$', views.sarisstd6, name="sarisstd6"),
    url(r'^saris_std7/$', views.sarisstd7, name="sarisstd7"),
    
    path("login/", views.loginPage, name = 'login'),
    path("logout/", views.logoutUser, name = 'logout'),
    path("signup/", views.signupPage, name = 'signup'),
    path("primaryregister/", views.primaryregisterPage, name = 'primaryregisterPage'),
    path("secondaryregister/", views.secondaryregisterPage, name = 'secondaryregisterPage'),
    path("techregister/", views.techschoolregisterPage, name = 'techschoolregisterPage'),
    path('user/', views.userPage, name = "userPage"),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="student_results/password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="student_results/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="student_results/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="student_results/password_reset_done.html"), 
        name="password_reset_complete"),   
    
]
