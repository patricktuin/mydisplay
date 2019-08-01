from django.contrib import admin

from displays.models import MyDisplayModel, Line, Display

admin.site.register(Line)


class LineinLine(admin.StackedInline):
    model = Line
    extra = 0


class MyDisplayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['model', ]}),
        ('Display information', {'fields': ['serial_number', 'friendly_name', 'font_size', 'customer', ]}),
    ]
    inlines = [LineinLine]


admin.site.register(MyDisplayModel)
admin.site.register(Display, MyDisplayAdmin)
