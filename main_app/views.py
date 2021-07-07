from main_app.models import Widget
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Widget
from .forms import WidgetForm



# Define the home view
def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm
    return render(request, 'index.html', {'widgets' : widgets, 'widget_form' : widget_form })

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('index')

def delete_widget(request, widget_id):
    w = Widget.objects.get(id=widget_id)
    w.delete()
    return redirect('index')
