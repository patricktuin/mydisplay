from django.forms import ModelForm, ModelChoiceField, Form, Select, Textarea, ChoiceField, ModelMultipleChoiceField, \
    RadioSelect

from displays.models import Line, MyDisplayModel, Display, Topic

TEXT_WIDGET = {'cols': 20, 'rows': 5, 'class': 'form-control'}
SELECT_WIDGET = {'class': 'form-control'}


class LineChoiceForm(ModelForm):
    # topics = ModelChoiceField(queryset=Topic.objects.all())
    # # lines = Line.objects.filter(display__serial_number=1234)
    # lines = ModelChoiceField(queryset=Line.objects.filter(display__serial_number=1234))

    class Meta:
        model = Line
        exclude = ('id', 'display')

        # widgets = {
        #     'topic': Select(attrs=SELECT_WIDGET),
        #     'lines': Select(attrs=SELECT_WIDGET)
        #     #
        # }

    # print(display)
    # for line in display.lines.all():
    #     print(line)
