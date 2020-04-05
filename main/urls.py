from django.urls import path,include,reverse_lazy
from .views import  homeview,load_all_country,updateCountry,updateNewCase
app_name='main'
urlpatterns = [
path('api/',homeview,name='apihome'),
path('load/',load_all_country,name='load'),
path('update/id=<int:id>',updateCountry,name='update'),
path('update/case/id=<int:id>',updateNewCase,name='updatecase'),
]
