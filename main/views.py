from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #messages.info(self.request, "hello http://example.com")
        return context
