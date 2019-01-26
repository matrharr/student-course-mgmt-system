from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from students import views

urlpatterns = [
    path('', views.StudentList.as_view()),
    path('<int:pk>/', views.StudentDetail.as_view()),
    path('<int:pk>/courses/', views.StudentCoursesDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
