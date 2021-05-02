
from django.conf.urls import url
from . import views

urlpatterns = [
    
    
      url(r'^api/state/$',views.CountriesViewSet.as_view({'get': 'state'})),
      url(r'^api/image/$',views.ImageView.as_view()),
   
]
