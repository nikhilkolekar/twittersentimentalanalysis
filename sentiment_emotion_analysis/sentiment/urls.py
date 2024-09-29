from django.urls import path, re_path
from . import views

app_name = 'sentiment'

urlpatterns = [
    re_path(r'^$', views.sentiment_analysis, name="sentiment_analysis"),
    re_path(r'^type/$', views.sentiment_analysis_type, name="sentiment_analysis_type"),
    re_path(r'^import/$', views.sentiment_analysis_import, name="sentiment_analysis_import"),
]
