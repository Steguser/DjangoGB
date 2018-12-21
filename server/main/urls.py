from django.urls import path
from main.views import (
    main_view, contacts_view, about_view
)

app_name = "main"

urlpatterns = [
    path('', main_view, name="index"),
    path('contacts/', contacts_view, name="contacts"),
    path('about/', about_view, name="about"),
]
