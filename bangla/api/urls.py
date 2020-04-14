from django.contrib import admin
from django.urls import path,include
from bangla.api import views
urlpatterns = [
    path('bangladash-division-create-or-update/',views.CrateOrUpdate),
    path('bangladash/divisions/',views.BangladeshDivisions.as_view()),
]
