from django.urls import path
from . import views

urlpatterns=[
    path('',views.getData),
    path('add/',views.addItem),
    path('add/<str:id>',views.update),
    path('delete/<str:id>',views.delete)

]