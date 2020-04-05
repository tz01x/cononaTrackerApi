from django.urls import path,include,reverse_lazy
from .views import  homeview,load_all_country,updateCountry,updateNewCase,CreateNewCase,deleteCase
app_name='main'
urlpatterns = [
path('api/',homeview,name='apihome'),
path('load/',load_all_country,name='load'),
path('update/id=<int:id>',updateCountry,name='update'),
path('update/id=<int:id>/create/case',CreateNewCase,name='createcase'),
path('update/case/id=<int:id>',updateNewCase,name='updatecase'),
path('update/country/<int:country_id>/case/<int:case_id>',deleteCase,name='deletecase'),
]
