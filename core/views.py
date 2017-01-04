# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages


User = get_user_model()


class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


