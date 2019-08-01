from displays.models import Display


def check_displays(request):
    if request.user.is_authenticated:
        displays = Display.objects.filter(customer__user=request.user)
        display_list = []
        for display in displays:
            display_list.append(display.serial_number)
    else:
        display_list = []
    return {'displays': display_list}
