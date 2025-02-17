from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import GoogleLogin

urlpatterns= [
    path('drugsRecords/',views.getdrugsRecordsList),
    path('drugRecords/<str:pk>/',views.getsingleRecord),
    path('interactingDrugs?drugName=<str:name>',views.interactingDrugs),
    path('createDrugRecord', views.createDrugRecord),
    path('updateDrugRecord/<str:pk>/', views.updateDrugRecord),
    path('token/obtain/', GoogleLogin.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('deleteReminders/<str:pk>',views.deleteReminders),
    path('todayReminders/<str:date>',views.todayReminders),
    path('hospitalDepartments/', views.hospitalDepartments),
    path('takeRecords',views.takeRecords)
]