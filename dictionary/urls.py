from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls", namespace="users")),
    path('', include("EnglishDictionary.urls", namespace="EnglishDictionary")),
    path('words/', include("words.urls", namespace="words")),
]
