from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView

from accounts.views import SettingsView, DisplayListView, DisplayLineUpdateView, DisplayLineCreateView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('accounts:login')), name='logout'),
    # path('add-line/<int:pk>', DisplayLineCreateView.as_view(), name='add-line'),
    path('settings/<int:pk>', DisplayLineUpdateView.as_view(), name='settings'),
    path('', DisplayListView.as_view(), name='displays')
]
