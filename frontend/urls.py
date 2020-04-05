

from django.urls import path,include
from frontend import  views
app_name='frontend'
urlpatterns=[
path('',views.display,name='home'),
path('about/',views.About,name='about'),
path('details/<str:name>/',views.details,name='details')
]
