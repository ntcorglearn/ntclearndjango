from django.urls import path
from . import views

app_name = 'elitexp'  # Optional: for namespacing URLs

urlpatterns = [
    # Define your app's URLs here
    path("", views.index, name="index")
]