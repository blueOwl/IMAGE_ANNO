from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
     HomePageView,
)

urlpatterns = [
 url(r"^$", HomePageView.as_view(), name="home"),
 url(r"^detail$", TemplateView.as_view(template_name='main/detailDoc.html'), name="detailDoc"),
 url(r"^examples$", TemplateView.as_view(template_name='main/examples.html'), name="examples"),
]
