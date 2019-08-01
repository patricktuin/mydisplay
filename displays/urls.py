from django.urls import path
from displays.views import AddLineView

app_name = 'displays'

urlpatterns = [
    path('<int:pk>', AddLineView.as_view(), name='index'),

]
