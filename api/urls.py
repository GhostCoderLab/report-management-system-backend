from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.ReportListView.as_view()),
    path('reports/<int:id>/', views.ReportDetailView.as_view()),
]