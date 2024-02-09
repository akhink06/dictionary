from django.urls import path , include
from words import views

app_name = "words"

urlpatterns = [
    path('create/',views.create_word, name="create_word"),
    path('',views.search, name="search"),
]
