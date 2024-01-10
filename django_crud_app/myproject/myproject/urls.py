from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', views.question_list, name='question_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/new/', views.question_new, name='question_new'),
    path('question/<int:pk>/edit/', views.question_edit, name='question_edit'),
    path('question/<int:pk>/delete/', views.question_delete, name='question_delete'),
]

