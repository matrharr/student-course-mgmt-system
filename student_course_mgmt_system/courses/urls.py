from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from courses import views

urlpatterns = [
    path('', views.CourseList.as_view()),
    path('<int:pk>/', views.CourseDetail.as_view()),
    path('<int:pk>/students/', views.CourseStudentsDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
