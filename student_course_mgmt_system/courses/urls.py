from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from courses import views

urlpatterns = [
    url('', views.CourseList.as_view()),
    url('<int:pk>/', views.CourseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
