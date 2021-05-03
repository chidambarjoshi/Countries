
from django.conf.urls import url
from . import views

urlpatterns = [
    
    
      url(r'^api/state/$',views.CountriesViewSet.as_view({'get': 'state'})),
      url(r'^api/image/$',views.ImageView.as_view()),
      url(r'^api/video/$',views.videoview.as_view({'get':'list'})),
      url(r'^api/video_post/$',views.videoview.as_view({'post':'videoup'})),
   
]
