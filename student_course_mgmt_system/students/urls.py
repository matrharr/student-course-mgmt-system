from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from students import views

urlpatterns = [
    url('', views.StudentList.as_view()),
    url('<int:pk>/', views.StudentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
