from django.urls import path , include
from EnglishDictionary import views

app_name = "EnglishDictionary"

urlpatterns = [
    path('',views.index, name="index"),
]
