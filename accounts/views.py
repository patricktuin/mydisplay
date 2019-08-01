from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView, CreateView
from django.db import transaction
from accounts.models import Customer
from accounts.forms import LineForm, DisplayLineFormSet
from topics.models import Topic
from displays.models import MyDisplayModel, Display, Line

from displays.forms import LineChoiceForm

from main.context_processors import check_displays


class LoginView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/login.html'


class DisplayListView(LoginRequiredMixin, ListView):
    model = Display

    template_name = 'accounts/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data
    #     return context

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user.customer)


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/settings.html'

    success_url = '/accounts/settings/'

    # display = MyDisplayModel.objects.get(pk=1)
    # lines = display.lines.all()

    def get_context_data(self, **kwargs):
        display = MyDisplayModel.objects.get(display__serial_number=self.kwargs['serial_number'])
        context = {
            'display_properties': '',
            'topics': '',
            'display': display
        }
        return context

    # display = MyDisplayModel.objects.get(pk=1)
    # display_lines = display.lines.count()
    # for lines in display:
    #     print(lines)


class DisplayList(ListView):
    model = Display


class DisplayCreate(CreateView):
    model = Display
    fields = ['friendly_name']


class DisplayLineCreateView(CreateView):
    model = Display
    template_name = 'accounts/settings.html'
    fields = ['friendly_name']

    def get_success_url(self):
        return '/accounts/'

    def get_context_data(self, **kwargs):
        data = super(DisplayLineCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = DisplayLineFormSet(self.request.POST)
        else:
            data['lines'] = DisplayLineFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()

        lines = context['lines']
        with transaction.atomic():
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
        return super(DisplayLineCreateView, self).form_valid(form)

    def inform_valid(self, form):
        print('Invalid')
        return super().form_invalid(form)


class DisplayLineUpdateView(LoginRequiredMixin, UpdateView):
    model = Display
    template_name = 'accounts/settings.html'
    fields = ['friendly_name', 'font_size', ]

    def get_success_url(self):
        return '/accounts/settings/{}'.format(self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        display = Display.objects.get(pk=self.kwargs['pk'])

        # Check if user is permitted to see and update the values of the display
        if display.serial_number not in check_displays(self.request)['displays']:
            raise PermissionDenied

        data = super(DisplayLineUpdateView, self).get_context_data(**kwargs)
        data['display'] = display

        if self.request.POST:
            data['lines'] = DisplayLineFormSet(self.request.POST, instance=self.object)
        else:
            data['lines'] = DisplayLineFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
        messages.success(self.request, 'Uw aanpassingen zijn opgeslagen')
        return super(DisplayLineUpdateView, self).form_valid(form)

    def inform_valid(self, form):
        print('Invalid')
        messages.error(self.request, 'Uw aanpassingen zijn niet opgeslagen')
        return super().form_invalid(form)

