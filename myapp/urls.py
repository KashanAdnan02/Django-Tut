from django.urls import path, include

urlpatterns = [
    path('', include("home.urls")),
    path('about', include("about.urls")),
    path('contact', include("contact.urls")),
]