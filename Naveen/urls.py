from django.urls import path
from . import views
urlpatterns=[
   path('',views.SRS,name='home'),
   # path('', views.good, name='1412'),
   # path('Thirdlargest/',views.Thirdlargest,name='Thirdlargest')
   #  path('',views.good,name='1412'),
   path('SRS/', views.SRS, name='SRS'),
]