from django.urls import path

from . import views

app_name = 'wifi_setup'
urlpatterns = [
    path('', views.index, name='index'),
    path('form-submit', views.form_submit, name='form_submit'),
    path('live', views.live, name='live'),
]