from django.urls import path,include
# from .views import (getusername,MyMessagesView,
#                 MyMessagesView2,createMessage)
app_name='main_api'
from main.api import  views
urlpatterns = [
    # path('getusername/',getusername),
    # path('myessages/',MyMessagesView.as_view())
    # path('testmyessages/',MyMessagesView),
    path('create_data/',views.createMessage),
    path('get-data/country=<str:name>/',views.CountryDetails,name='getcountry'),
    path('all-countries-state/',views.MyMessagesView2.as_view(),name='getalldata'),
]
