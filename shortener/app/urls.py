from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('reports', views.ReportViewSet, basename='reports')

urlpatterns = [
    path('shorten/', views.ShortenAPIView.as_view(), name='shorten'),
    path('r/<slug:short>/', views.URLAPIView.as_view(), name='get-url'),
    path('today_report/<int:url_id>/', views.TodayReportAPIView.as_view(), name='today-report'),
]

urlpatterns += router.urls