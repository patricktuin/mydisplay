from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, FormView, UpdateView

from displays.models import Topic, Display, Line
from displays.forms import LineChoiceForm


def add_line(request):
    print('Added a line')
    return HttpResponse("You're voting on questio")


class AddLineView(UpdateView):
    model = Line
    form_class = LineChoiceForm
    template_name = 'displays/line_choice.html'
    success_url = '/display/1'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.instance.serial_number = 1234
        return super().form_valid(form)
