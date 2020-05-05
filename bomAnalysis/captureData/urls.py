from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('history/',views.history,name='history'),
    path('analysis/',views.analysis,name='analysis'),
    path('recent/<int:duration>/days',views.recent_day,name='recent_day'),
    path('recent/<int:duration>/hours',views.recent_hour,name='recent_hour'),
    path('recent/<int:duration>/weeks',views.recent_week,name='recent_week'),
]