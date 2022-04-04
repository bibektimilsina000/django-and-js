from django.shortcuts import render

from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = "home.html"

